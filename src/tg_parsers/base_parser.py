from datetime import datetime
import json

from telethon.tl.patched import Message
from telethon.tl.types import MessageEntityTextUrl, MessageEntityUrl, MessageEntityMention

from src.blockchains import Blockchain


class TgParser:
    
    _CHANEL_ID: int
    _NETWORK: Blockchain

    
    def __init__(self, message: Message):
        self.message_text = message.message
        self.message = self.message_text.split('\n')

        self.message_hidden_links = self._get_message_hidden_links(message)

        self.token_name = self.find_token_name()
        self.token_symbol = self.find_token_symbol()
        self.token_address = self.find_token_address()
        self.token_pool_address = self.find_token_pool_address()
        self.portal_url = self.find_chat_url()
        self.created_at = datetime.now().isoformat()

    @classmethod
    def get_channel_id(cls) -> int:
        if cls._CHANEL_ID:
            return cls._CHANEL_ID
        raise NotImplementedError

    @classmethod
    def get_network(cls) -> Blockchain:
        if cls._NETWORK:
            return cls._NETWORK
        raise NotImplementedError

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

    @staticmethod
    def _get_message_hidden_links(message: Message) -> dict:

        urls = {}

        for entity, text in message.get_entities_text():
            if isinstance(entity, MessageEntityTextUrl):
                ''' Text links: [LINK](https://example.com) '''
                key = text
                if key in urls:
                    urls[text].append(entity.url)
                else:
                    urls[text] = [entity.url]

            elif isinstance(entity, MessageEntityUrl):
                ''' URLs: t.me/some_link or example.com'''
                url_text = text

                if any(url_text.startswith(start) for start in ('https://t.me/', 'https://telegram.me/')):
                    link = url_text
                    key = 'TG'
                elif url_text.startswith('https://'):
                    link = url_text
                    key = link
                elif any(url_text.startswith(start) for start in ('t.me/', 'telegram.me/')):
                    link = f'https://{url_text}'
                    key = 'TG'
                else:
                    link = f'https://{url_text}'
                    key = link

                if link.endswith('/'):
                    link = link[:-1]

                if key in urls:
                    urls[key].append(link)
                else:
                    urls[key] = [link]

            elif isinstance(entity, MessageEntityMention):
                ''' Telegram names: @some_name '''
                key = 'TG'
                link = f'https://t.me/{text[1:]}'
                if key in urls:
                    urls[key].append(link)
                else:
                    urls[key] = [link]

        return urls

        
    def dict(self) -> dict:    
        return {
            "token_address": self.token_address,
            "token_pool_address": self.token_pool_address,
            "token_name": self.token_name,
            "token_symbol": self.token_symbol,
            "dex_name": None,
            "network": self._NETWORK,
            "created_at": self.created_at,
            "portal_url": self.portal_url,
            "creator": None,
        }

    def json(self) -> str:
        return json.dumps(self.dict())
    
    def is_correct_to_save(self) -> None:
        if self.token_address:
            return True
        else:
            return False
