import asyncio
import os

from dotenv import load_dotenv

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from pyrogram import utils


import src.tg_parsers
from src.tg_handlers.register_handler import register_handlers
from src.tg_parsers.register_parsers import ALL_PARSERS
from src.tg_parsers.base_parser import TgParser
from src.loguru_config import logger


# def get_peer_type_new(peer_id: int):
#     peer_id_str = str(peer_id)

#     if not peer_id_str.startswith('-'):
#         return "user"
#     elif peer_id_str.startswith('-100'):
#         return "channel"
#     else:
#         return "chat"

# utils.get_peer_type = get_peer_type_new

load_dotenv(".env")

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")

# Инициализация клиента
app = Client("tg_app", api_id=API_ID, api_hash=API_HASH, phone_number=PHONE_NUMBER)


# ==========================================


async def message_processing(
        listener: Client,
        parsed_data: dict
) -> None:
    logger.info(f"Parsed token data: {parsed_data}")
    await listener.send_message('self', f"Parsed token data: {parsed_data}")
    # Дальнейшая обработка данных


# ==========================================


# @app.on_message()
# async def channel_message_handler(client, message):
#     try:
#         chat_info = await client.get_chat(message.chat.id)
#         print(f"Chat info: {chat_info.title}")
#     except Exception as e:
#         print(f"Error: {e}")
    
#     if message.chat.id in [-1002008381526, -1001802262411, -1002070002579]:
#         print(f'YES: {message.chat.id}')
#         text = message.text or "Медиа/файл"
#         logger.info(f"Новое сообщение из канала {message.chat.title} {message.link} {message.chat.username}: {text}")
#     else:
        # print(f'NO: {message.chat.id}')

# ==========================================



if __name__ == "__main__":
    # Регистрируем все хэндлеры
    # register_handlers(app, worker)
    register_handlers(app)

    # Запускаем бота
    app.run()
