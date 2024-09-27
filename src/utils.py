import re

from src.tg_parsers.register_parsers import ALL_PARSERS


TG_PATTERN = re.compile(r"(?:https?://)?(?:www\.)?(?:t(?:elegram)?\.(?:org|me|dog))/(?:joinchat/|\+)?\S+")
TW_PATTERN = re.compile(r"(?:https?://)?(?:www\.)?(?:x|twitter).com/\S+")


def is_url(text: str) -> bool:
    pattern = re.compile(r"^http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    return re.match(pattern, text) is not None

def find_tg_url(text: str) -> str | None:
    """
    Find telegram link in text. If not found, return None
    :param text:
    :return:
    """
    if text is None or len(text) < 1:
        return None

    res = TG_PATTERN.search(text)

    if res is None:
        return None

    return re.sub(r"[\s\\/.(),;[\]{}]+$", "", res.group())

def is_needed_chat(chat_id: int):
    if chat_id in ALL_PARSERS.get_parsers():
        return True
    return False
