from typing import Any
from typing import Awaitable
from typing import Callable
from typing import Dict

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
        await self.logger.ainfo(event=event, data=data)
        return await handler(event, data)


__all__ = ["LoggerMiddleware"]
