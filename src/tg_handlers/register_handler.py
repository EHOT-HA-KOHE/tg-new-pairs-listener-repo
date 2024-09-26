from pyrogram import Client
from pyrogram.handlers import RawUpdateHandler

from .handler import chanel_handler


def register_handlers(listener: Client) -> None:
    listener.add_handler(RawUpdateHandler(callback=chanel_handler))
