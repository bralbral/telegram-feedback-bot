from typing import Any, Awaitable, Callable, Dict

import structlog
from aiogram import BaseMiddleware
from aiogram.types import Message


class LoggerMiddleware(BaseMiddleware):
    def __init__(self, logger: structlog.BoundLogger) -> None:
        self.logger = logger

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        self.logger.info(
            "telegram_message_received",
            message_id=event.message_id,
            chat_id=event.chat.id,
            content_type=event.content_type,
            from_user_id=event.from_user.id if event.from_user else None,
        )
        return await handler(event, data)


__all__ = ["LoggerMiddleware"]
