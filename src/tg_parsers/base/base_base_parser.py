from pyrogram.types import Message

from src.blockchains import Blockchain
from ..base_parser import TgParser


class BaseTgParser(TgParser):

    _NETWORK = Blockchain.Base
    
    def __init__(self, message: Message) -> None:
        super().__init__(message)
