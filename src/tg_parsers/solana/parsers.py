from telethon.tl.types import Message

from src.tg_parsers.register_parsers import register_parser
from src.utils import find_tg_url
from .base_solana_parser import SolanaTgParser


@register_parser
class SolanaSolanaScanner(SolanaTgParser):
    """ https://t.me/solanascanner """
    
    _CHANEL_ID = -1002023951506

    def __init__(self, message: Message) -> None:
        super().__init__(message)

    def find_token_name(self) -> str | None:
        for line in self.message:
            if "🏷 Name:" in line:
                return line.split("🏷 Name: ")[-1]

        return None

    def find_token_symbol(self) -> str | None:
        for line in self.message:
            if "💲 Symbol:" in line:
                return line.split("💲 Symbol: ")[-1].split('$')[-1]

        return None

    def find_token_address(self) -> str | None:
        for line, text in enumerate(self.message):
            if "🏠 Address:" in text:
                return self.message[line + 1]
        return None

    def find_token_pool_address(self) -> str | None:
        return None

    def find_chat_url(self) -> str | None:
        skip = True

        for line in self.message:
            if "📱 Socials" in line:
                skip = False
                continue

            if skip:
                continue

            if "None" in line:
                break

            if "└─ X:" in line:
                break

            url = find_tg_url(line)

            if url is not None:
                return url

        return None
