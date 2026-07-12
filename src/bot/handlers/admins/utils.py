import re
from typing import Literal

from aiogram.types import Message

ID_PATTERNS: dict[str, re.Pattern[str]] = {
    "chat_id": re.compile(r"#id(\d+)\b"),
    "message_id": re.compile(r"#msgid(\d+)\b"),
}


def extract_id(message: Message, id_type: Literal["chat_id", "message_id"]) -> int:
    """Extract an ID embedded in a bot-forwarded message."""
    text = message.text or message.caption or ""
    match = ID_PATTERNS[id_type].search(text)
    if match is None:
        raise ValueError(f"Cannot match {id_type}")

    return int(match.group(1))


__all__ = ["extract_id"]
