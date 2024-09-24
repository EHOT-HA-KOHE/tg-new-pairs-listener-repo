import os

from dotenv import load_dotenv

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from pyrogram import utils

import src.tg_parsers
from src.loguru_config import logger
from src.tg_parsers.register_parsers import TRACKED_CHANNELS


def get_peer_type_new(peer_id: int):
    peer_id_str = str(peer_id)

    if not peer_id_str.startswith('-'):
        return "user"
    elif peer_id_str.startswith('-100'):
        return "channel"
    else:
        return "chat"

utils.get_peer_type = get_peer_type_new



print(f"{TRACKED_CHANNELS = }")

load_dotenv(".env")

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")

# Инициализация клиента
app = Client("tg_app", api_id=API_ID, api_hash=API_HASH, phone_number=PHONE_NUMBER)


# Процесс обработки сообщений
async def message_processing(
    listener: Client,
    parser,
) -> None:
    logger.info(f"Token data: {parser.dict()}")


# Создание обработчика сообщений для конкретного парсера
def create_handler(parser_cls):
    async def handler(client: Client, message: Message) -> None:
        logger.info(f"message from {parser_cls.__name__}")

        # Передаем message при создании экземпляра класса
        parser_instance = parser_cls(message)

        # Обрабатываем сообщение с использованием парсера
        await message_processing(client, parser_instance)

    return handler


# Регистрация обработчиков для отслеживаемых каналов
def register_tg_parsers(client: Client) -> None:
    parsers = TRACKED_CHANNELS.values()  # Список парсеров

    for parser_class in parsers:
        # Создаем обработчик для каждого парсера
        handler = create_handler(parser_class)

        logger.info(
            f"Channel - {parser_class.__name__}, ID - {parser_class._CHANEL_ID}"
        )

        # Добавляем обработчик для сообщений от определенного канала
        client.add_handler(
            MessageHandler(
                handler, filters.chat(parser_class._CHANEL_ID)  # Фильтруем по ID канала
            )
        )




# @app.on_message(filters.channel)
# async def channel_message_handler(client: Client, message: Message):
#     print(f"Received message from chat ID: {message.chat.id}, chat title: {message.chat.title}\n")
#     channel_id = message.chat.id
#     if channel_id in TRACKED_CHANNELS:
#         parser_class = TRACKED_CHANNELS[channel_id]
#         logger.info(f'{parser_class.__name__ = }')
    #     logger.info(f"New mes from {parser_class.__name__} with id: {channel_id}")

    #     # Инициализируем класс и передаем сообщение
    #     parser_instance = parser_class(message)

    #     # Пример вызова метода
    #     info = parser_instance.dict()
    #     logger.info(f"Info: {info}")


# Основной блок запуска приложения
if __name__ == "__main__":
    logger.info("Бот запущен...")

    # app.start()
    # test()
    # app.stop()

    register_tg_parsers(app)
    app.run()


# @app.on_message(filters.channel & filters.chat(CHANNEL_ID))
# async def channel_message_handler(client, message):
#     text = message.text or "Медиа/файл"
#     logger.info(f"Новое сообщение из канала {message.chat.title} {message.link} {message.chat.username}: {text}")
# await client.send_message(message.chat.id, f"Получено сообщение из канала: {text}")
