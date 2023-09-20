from aiogram.filters import BaseFilter
from aiogram.types import Message


class FilterByChatID(BaseFilter):
    """
    Filter events from chat declared in config.yaml
    """

    async def __call__(self, message: Message, chat_id: int) -> bool:
        return bool(message.chat.id == chat_id)


__all__ = ["FilterByChatID"]
