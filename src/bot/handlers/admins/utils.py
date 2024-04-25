import re
from typing import Literal

from aiogram.types import Message

ID_PATTERN = re.compile(pattern=r"#id\d{1,}[\s]?")
MESSAGE_ID_PATTERN = re.compile(pattern=r"#msgid\d{1,}[\s]?")


def extract_id(message: Message, id_type: Literal["chat_id", "message_id"]) -> int:
    """
    Extract #id12345678 or #msgid12345678u addition from message text start
    :param id_type:
    :param message:
    :return:
    """

    if id_type == "chat_id":
        pattern = ID_PATTERN
        prefix = "#id"
    elif id_type == "message_id":
        pattern = MESSAGE_ID_PATTERN
        prefix = "#msgid"
    else:
        raise ValueError(f"Unknown id_type: {id_type}")

    text = message.text if message.text else message.caption
    matches = pattern.findall(text)
    if len(matches) == 0:
        raise ValueError(f"Cannot match {prefix}")

    _id = int(str(matches[0]).replace(prefix, "").strip())

    return _id


__all__ = ["extract_id"]
