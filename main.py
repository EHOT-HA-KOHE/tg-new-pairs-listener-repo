import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import Message

import src.tg_parsers

from src.loguru_config import logger
from src.tg_parsers.register_parsers import TRACKED_CHANNELS

print(f'{TRACKED_CHANNELS = }')


load_dotenv('.env')


API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
PHONE_NUMBER = os.getenv('PHONE_NUMBER')
CHANNEL_ID = -1002106686989


# Инициализация клиента
app = Client("tg_app", api_id=API_ID, api_hash=API_HASH, phone_number=PHONE_NUMBER)



@app.on_message(filters.channel)
async def channel_message_handler(client: Client, message: Message):
    channel_id = message.chat.id
    if channel_id in TRACKED_CHANNELS:
        parser_class = TRACKED_CHANNELS[channel_id]
        logger.info(f"New mes from {parser_class.__name__} with id: {channel_id}")
        
        # Инициализируем класс и передаем сообщение
        parser_instance = parser_class(message)
        
        # Пример вызова метода
        info = parser_instance.dict()
        logger.info(f"Info: {info}")


# @app.on_message(filters.channel & filters.chat(CHANNEL_ID))
# async def channel_message_handler(client, message):
#     text = message.text or "Медиа/файл"
#     logger.info(f"Новое сообщение из канала {message.chat.title} {message.link} {message.chat.username}: {text}")
    # await client.send_message(message.chat.id, f"Получено сообщение из канала: {text}")


if __name__ == '__main__':
    logger.info("Бот запущен...")
    app.run()
