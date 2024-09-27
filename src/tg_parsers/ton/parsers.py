import re

from telethon.tl.types import Message

from src.tg_parsers.register_parsers import register_parser
from .base_ton_parser import TonTgParser


@register_parser
class TonNewTonPairs(TonTgParser):
    """ https://t.me/NewTonPairs """
    
    _CHANEL_ID = -1002070002579

    def __init__(self, message: Message) -> None:
        super().__init__(message)

    def find_token_name(self) -> str | None:
        match = re.search(r'^(\w+)\s*\(', self.message[0])
        if match:
            return match.group(1).strip()
        return None

    def find_token_symbol(self) -> str | None:
        match = re.search(r'\(([^)]+)\)', self.message[0])
        if match:
            return match.group(1).strip()
        return None

    def find_token_address(self) -> str | None:
        match = re.search(r'CA:\s*(\S+)', self.message[2])
        if match:
            return match.group(1).strip()
        return None

    def find_token_pool_address(self) -> str | None:
        match = re.search(r'Pool:\s*(\S+)', self.message[1])
        if match:
            return match.group(1).strip()
        return None

    def find_chat_url(self) -> str | None:
        return self.message_hidden_links.get("👥 Telegram", [None])[0]
