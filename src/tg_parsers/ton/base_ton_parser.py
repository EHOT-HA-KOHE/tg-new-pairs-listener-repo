from pyrogram.types import Message

from src.blockchains import Blockchain
from ..base_parser import TgParser


class TonTgParser(TgParser):

    _NETWORK = Blockchain.Ton
    
    def __init__(self, message: Message) -> None:
        super().__init__(message)
