import re

from telethon.tl.types import Message

from src.tg_parsers.register_parsers import register_parser
from src.utils import find_tg_url
from .base_test_parser import TestTgParser


@register_parser(test=True)
class TestParser(TestTgParser):
    """ TEST CHANNEL """
    
    _CHANEL_ID = -1002125707421

    def __init__(self, message: Message) -> None:
        super().__init__(message)

    def find_token_name(self) -> str | None:
        match = re.search(r'🪙(.*?)\(', self.message[2])
        if match:
            return match.group(1).strip()
        return None

    def find_token_symbol(self) -> str | None:
        match = re.search(r'\(s*(.*?)s*\)', self.message[2])
        if match:
            return match.group(1).strip()
        return None

    def find_token_address(self) -> str | None:
        if '🔖' in self.message[3]:
            return self.message[3].split('🔖')[-1].strip()
        return None

    def find_token_pool_address(self) -> str | None:
        return None

    def find_chat_url(self) -> str | None:
        return None
    