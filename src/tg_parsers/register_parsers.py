from src.loguru_config import logger


TRACKED_CHANNELS = {}

def track_channel(cls):
    """ Decorator for add parser classes """
    if hasattr(cls, '_CHANEL_ID'):
        channel_id = getattr(cls, '_CHANEL_ID')
        TRACKED_CHANNELS[channel_id] = cls
        logger.info(f"Channel {cls.__name__} with id {channel_id} added to tracking addresses")
    else:
        raise AttributeError(f"{cls.__name__} haven`t _CHANEL_ID")
    return cls