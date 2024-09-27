from telethon.tl.types import Message

from src.blockchains import Blockchain
from ..base_parser import TgParser


class TestTgParser(TgParser):

    _NETWORK = Blockchain.Test
    
    def __init__(self, message: Message) -> None:
        super().__init__(message)
