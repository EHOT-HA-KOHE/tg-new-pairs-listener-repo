import re

from telethon.tl.types import Message

from src.tg_parsers.register_parsers import register_parser
from .base_ethereum_parser import EthTgParser


@register_parser
class EthiTokenEthereum(EthTgParser):
    """ https://t.me/iTokenEthereum """

    _CHANEL_ID = -1001696523760

    def __init__(self, message: Message) -> None:
        self._post_types = {'Deployed', 'Verified', 'Launching', 'Locked'}
        super().__init__(message)

    def _is_correct_post(self, line) -> bool:
        if any(post_type in line for post_type in self._post_types):
            return True
        else:
            return False

    def find_token_name(self) -> str | None:
        match = re.search(r'\(([^)]+)\)', self.message[0])
        if match:
            return match.group(1).strip()
        return None

    def find_token_symbol(self) -> str | None:
        line_without_name = self.message[0].split("(")[0].strip()
        return line_without_name.split(" ")[-1].strip()

    def find_token_address(self) -> str | None:
        if not self._is_correct_post(self.message[0]):
            return None

        for line in self.message:
            if line.startswith("CA: "):
                return line.split('CA: ')[-1].strip()

        return None
    
    def find_token_pool_address(self) -> str | None:
        return None

    def find_chat_url(self) -> str | None:
        if not self._is_correct_post(self.message[0]):
            return None

        if "Deployed:" in self.message[0]:
            return None

        if any("TG 🤷‍♂️" in line for line in self.message[4:14]):
            return None

        else:
            return self.message_hidden_links.get("TG", [None])[0]
