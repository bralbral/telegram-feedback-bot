import re

from aiogram.types import Message

ID_PATTERN = re.compile(pattern=r"#id\d{1,}[\s]?")


def extract_id(message: Message) -> int:
    """
    Extract #id12345678 addition from message text start
    :param message:
    :return:
    """
    text = message.text if message.text else message.caption
    matches = ID_PATTERN.findall(text)
    if len(matches) == 0:
        raise ValueError("Cannot match #id")

    _id = int(str(matches[0]).replace("#id", "").strip())

    return _id


__all__ = ["extract_id"]
