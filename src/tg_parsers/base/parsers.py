from pyrogram.types import Message

from src.tg_parsers.register_parsers import track_channel
from .base_base_parser import BaseTgParser


# @track_channel
class BaseBaseNewPairsTrending(BaseTgParser):
    """ https://t.me/UnibotBaseScanner """

    _CHANEL_ID = -1002106686989

    def __init__(self, message: Message) -> None:
        super().__init__(message)

    def find_token_name(self) -> str | None:
        return self.message[1]

    def find_token_symbol(self) -> str | None:
        return self.message[1]

    def find_token_address(self) -> str | None:
        return self.message[1]

    def find_token_pool_address(self) -> str | None:
        return self.message[1]

    def find_chat_url(self) -> str | None:
        return self.message[1]
