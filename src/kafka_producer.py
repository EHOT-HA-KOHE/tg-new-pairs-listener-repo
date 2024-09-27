import os

from confluent_kafka import Producer


broker = os.getenv('KAFKA_BROKER', 'kafka:9092')

producer = Producer({'bootstrap.servers': broker})


def save_and_alarm_new_pool_by_kafka(
        token_address: str, token_pool_address: str | None, 
        token_name: str | None, token_symbol: str | None, 
        dex_name: str | None, network: str, 
        created_at: str, portal_url: str | None, creator: str | None
    ) -> None:

    data = {
        "token_address": token_address,
        "token_pool_address": token_pool_address,
        "token_name": token_name,
        "token_symbol": token_symbol,
        "dex_name": dex_name,
        "network": network,
        "created_at": created_at,
        "portal_url": portal_url,
        "creator": creator,
    }

    producer.produce('show-new-pool-ws', key='key', value=str(data))
    producer.produce('save-new-pool-to-db', key='key', value=str(data))

    producer.flush()
