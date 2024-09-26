from typing import Type, List, Dict
from dataclasses import dataclass, field

from src.loguru_config import logger
from src.tg_parsers.base_parser import TgParser


@dataclass
class Parsers:
    parsers: Dict[int, Type[TgParser]] = field(default_factory=dict)

    def add_parser(self, parser: Type[TgParser]) -> None:
        self.parsers[parser.get_channel_id()] = parser

    def get_parser(self, channel_id: int) -> Type[TgParser] | None:
        return self.parsers.get(channel_id)

ALL_PARSERS = Parsers()

def register_parser(parser: Type[TgParser]) -> Type[TgParser]:
    """Декоратор для регистрации парсера."""
    ALL_PARSERS.add_parser(parser)
    return parser


# Parsers(parsers={
# -1002008381526: <class 'src.tg_parsers.ethereum.parsers.EthVerifiedETHTokens'>, 
# -1001802262411: <class 'src.tg_parsers.solana.parsers.SolanaSolanaNewTokenMints'>, 
# -1002070002579: <class 'src.tg_parsers.ton.parsers.TonNewTonPairs'>
# })
