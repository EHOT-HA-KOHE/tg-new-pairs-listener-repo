from src.tg_parsers.register_parsers import ALL_PARSERS


def is_needed_chat(chat_id: int):
    if chat_id in ALL_PARSERS.parsers:
        return True
    return False
