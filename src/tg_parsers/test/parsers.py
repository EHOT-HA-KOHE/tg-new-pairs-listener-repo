from pyrogram.types import Message

from src.tg_parsers.register_parsers import register_parser
from .base_test_parser import TestTgParser


@register_parser
class TestParser(TestTgParser):
    """ https://t.me/solanatokenmints """
    
    _CHANEL_ID = -1002125707421

    def __init__(self, message: Message) -> None:
        super().__init__(message)

    def find_token_name(self) -> str | None:
        return self.message[0]

    def find_token_symbol(self) -> str | None:
        return self.message[0]

    def find_token_address(self) -> str | None:
        return self.message[0]

    def find_token_pool_address(self) -> str | None:
        return self.message[0]

    def find_chat_url(self) -> str | None:
        return self.message[0]
