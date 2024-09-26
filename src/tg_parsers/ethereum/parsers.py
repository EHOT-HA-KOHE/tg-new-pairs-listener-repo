from pyrogram.types import Message

from src.tg_parsers.register_parsers import register_parser
from .base_ethereum_parser import EthTgParser


@register_parser
class EthVerifiedETHTokens(EthTgParser):
    """ https://t.me/gm_verified """

    _CHANEL_ID = -1002008381526

    def __init__(self, message: Message) -> None:
        super().__init__(message)

    def find_token_name(self) -> str | None:
        header = self.message[0]
        name = header.split(" | ")[-1].strip()
        return name

    def find_token_symbol(self) -> str | None:
        header = self.message[0]
        symbol = header.split("#")[-1].strip().split(" ")[0]
        return symbol

    def find_token_address(self) -> str | None:
        return self.message[2].strip()
    
    def find_token_pool_address(self) -> str | None:
        return None

    def find_chat_url(self) -> str | None:
        if " TG" in self.message[4]:
            for entity in self.message_entity:
                if entity.type == MessageEntityType.TEXT_LINK:
                    res = find_tg_url(entity.url)
                    if res:
                        return res

        return None

