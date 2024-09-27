from telethon.tl.types import Message

from src.blockchains import Blockchain
from ..base_parser import TgParser


class SolanaTgParser(TgParser):

    _NETWORK = Blockchain.Solana
    
    def __init__(self, message: Message) -> None:
        super().__init__(message)
