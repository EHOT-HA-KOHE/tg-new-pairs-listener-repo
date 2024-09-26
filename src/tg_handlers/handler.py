from pyrogram import Client, raw

from src.loguru_config import logger
from src.utils import is_needed_chat


async def chanel_handler(listener: Client, update: raw.base.Update, *args) -> None:
    logger.debug(f"chanel_handler got update type: {type(update)}")

    if not any([
            isinstance(update, raw.types.UpdateNewChannelMessage),
            isinstance(update, raw.types.UpdateNewMessage)
    ]):
        return

    message = update.message
    peer_id = message.peer_id

    channel_id = message.peer_id.channel_id
    logger.info(f"message from -100{channel_id} channel")

    if not isinstance(peer_id, raw.types.PeerChannel):
        return

    chat_id = int(f"-100{peer_id.channel_id}")

    if not is_needed_chat(chat_id):
        logger.error(f"message from {chat_id} is not in channels_to_listen")
        return

    logger.info(f"message from {chat_id} is in channels_to_listen")
