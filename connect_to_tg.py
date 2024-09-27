import os

from dotenv import load_dotenv

from telethon import TelegramClient

from src.loguru_config import logger


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(BASE_DIR, 'telegram.env')

load_dotenv(env_path)

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")


if not API_ID or not API_HASH or not PHONE_NUMBER:
    raise ValueError("Invalid API_ID, API_HASH, or PHONE_NUMBER in telegram.env file.")


client = TelegramClient("tg_connection", API_ID, API_HASH)


async def connect_client():
    await client.start(phone=PHONE_NUMBER)
    logger.info("Successful authentication")

    if not await client.is_user_authorized():
        raise ValueError("Error for initializing the client. Invalid API_ID, API_HASH, or PHONE_NUMBER?")
    
    logger.info("Client TG connection - SUCCESSFUL!")


def get_client():
    return client


if __name__ == "__main__":
    import asyncio
    asyncio.run(connect_client())
