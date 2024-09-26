import json

from pyrogram.types import Message
from pyrogram.enums import MessageEntityType

from src.blockchains import Blockchain
# from src.kafka_producer import save_and_alarm_new_pool_by_kafka


class TgParser:
    
    _CHANEL_ID: int
    _NETWORK: Blockchain

    
    def __init__(self, message: Message):
        self.message_text = message.text or message.caption
        message_entities = message.entities or message.caption_entities

        self.message = self.message_text.split('\n')
        self.message_hidden_links = self._get_message_hidden_links(self.message_text, message_entities)

        self.token_name = self.find_token_name()
        self.token_symbol = self.find_token_symbol()
        self.token_address = self.find_token_address()
        self.token_pool_address = self.find_token_pool_address()
        self.portal_url = self.find_chat_url()

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
    def _get_message_hidden_links(text: str, entities: list) -> dict:
        urls = {}

        if entities is None:
            return {}

        for entity in entities:
            if entity.type == MessageEntityType.TEXT_LINK:
                ''' Text links: [LINK](https://example.com) '''
                key = text[entity.offset:entity.offset + entity.length]
                if key in urls:
                    urls[key].append(entity.url)
                else:
                    urls[key] = [entity.url]

            if entity.type == MessageEntityType.URL:
                ''' URLs: t.me/some_link or example.com'''
                url_text = text[entity.offset:entity.offset + entity.length]

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

            if entity.type == MessageEntityType.MENTION:
                ''' Telegram names: @some_name '''
                key = 'TG'
                link = f'https://t.me/{text[(entity.offset + 1):entity.offset + entity.length]}'
                if key in urls:
                    urls[key].append(link)
                else:
                    urls[key] = [link]

        return urls
        
    def dict(self) -> dict:
        return {
            "name": self.token_name,
            "symbol": self.token_symbol,
            "network": self._NETWORK,
            "token_address": self.token_address,
            "token_pool_address": self.token_pool_address,
            "creator": "Unknown",
            "portal_url": self.portal_url
        }

    def json(self) -> str:
        return json.dumps(self.dict())
    
    def save(self) -> None:
        # save_and_alarm_new_pool_by_kafka(self.dict())
        ...
