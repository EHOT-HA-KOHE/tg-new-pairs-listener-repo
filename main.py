from telethon import events

from connect_to_tg import client, PHONE_NUMBER

from src.loguru_config import logger
from src.kafka_producer import save_and_alarm_new_pool_by_kafka
from src.tg_parsers.register_parsers import ALL_PARSERS


async def main():
    await client.start(phone=PHONE_NUMBER)
    logger.info("Successful authentication")

    me = await client.get_me()
    logger.info(f"Logged in as {me.username}")

    @client.on(events.NewMessage(chats=ALL_PARSERS.get_parsers()))
    async def message_handler(event):
        channel_id = event.chat_id

        parser = ALL_PARSERS.get_parser(channel_id)

        if parser:
            logger.debug(f"Message from channel: {channel_id} - {event.chat.title}")

            parse_res = parser(event.message)
            logger.debug(parse_res.dict())

            if parse_res.is_correct_to_save():
                save_and_alarm_new_pool_by_kafka(**parse_res.dict())
            else:
                logger.debug("Dont save token! Have NOT token_address")

    await client.run_until_disconnected()


if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())
