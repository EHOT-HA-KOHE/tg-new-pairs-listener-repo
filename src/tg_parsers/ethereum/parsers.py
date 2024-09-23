from pyrogram.types import Message

from src.tg_parsers.register_parsers import track_channel
from .base_ethereum_parser import EthTgParser


@track_channel
class EthOttoETHDeployments(EthTgParser):
    """ https://t.me/OttoETHDeployments """

    _CHANEL_ID = -1001844431042

    def __init__(self, message: Message) -> None:
        super().__init__(message)

    def find_token_name(self) -> str | None:
        raise NotImplementedError

    def find_token_symbol(self) -> str | None:
        raise NotImplementedError

    def find_token_address(self) -> str | None:
        raise NotImplementedError

    def find_token_pool_address(self) -> str | None:
        raise NotImplementedError

    def find_chat_url(self) -> str | None:
        raise NotImplementedError
