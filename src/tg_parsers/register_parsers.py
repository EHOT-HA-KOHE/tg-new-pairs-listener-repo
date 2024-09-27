from typing import Type, List, Dict
from dataclasses import dataclass, field

from src.tg_parsers.base_parser import TgParser


TEST_MODE = False


@dataclass
class Parsers:
    main_parsers: Dict[int, Type[TgParser]] = field(default_factory=dict)
    test_parsers: Dict[int, Type[TgParser]] = field(default_factory=dict)

    def add_parser(self, parser: Type[TgParser], test: bool=False) -> None:
        if test:
            self.test_parsers[parser.get_channel_id()] = parser
        else:
            self.main_parsers[parser.get_channel_id()] = parser


    def get_parser(self, channel_id: int) -> Type[TgParser] | None:
        if res := self.main_parsers.get(channel_id):
            return res
        else:
            return self.test_parsers.get(channel_id)
    
    def get_parsers(self):
        return self.test_parsers if TEST_MODE else self.main_parsers


ALL_PARSERS = Parsers()


def register_parser(*args, **kwargs):
    """ Decorator for parser registration """
    test = kwargs.get("test", False)

    # Decorator without params
    if len(args) == 1 and callable(args[0]):
        parser = args[0]
        ALL_PARSERS.add_parser(parser)
        return parser

    # Decorator with params, example: "(test=True)"
    def wrapper(parser: Type[TgParser]) -> Type[TgParser]:
        ALL_PARSERS.add_parser(parser, test)
        return parser
    
    return wrapper
