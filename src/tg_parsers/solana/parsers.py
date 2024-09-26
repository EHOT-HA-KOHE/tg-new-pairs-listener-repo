from pyrogram.types import Message

from src.tg_parsers.register_parsers import register_parser
from .base_solana_parser import SolanaTgParser


@register_parser
class SolanaSolanaScanner(SolanaTgParser):
    """ https://t.me/solanascanner """
    
    _CHANEL_ID = -1002023951506
    # _CHANEL_ID = -1002125707421

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
