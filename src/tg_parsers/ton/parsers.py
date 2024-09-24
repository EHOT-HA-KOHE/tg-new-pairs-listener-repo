from pyrogram.types import Message

from src.tg_parsers.register_parsers import track_channel
from .base_ton_parser import TonTgParser


@track_channel
class TonNewTonPairs(TonTgParser):
    """ https://t.me/NewTonPairs """
    
    _CHANEL_ID = '-1002070002579'
    # _CHANEL_ID = -1002000050228

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
