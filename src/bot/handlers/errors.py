from typing import Optional

import aiogram.exceptions
from aiogram import Bot, Router
from aiogram.types import User
from aiogram.types.error_event import ErrorEvent

from src.config import Errors
from src.logger import logger

errors_router = Router(name="errors")


@errors_router.errors()  # type: ignore
async def error_handler(exception: ErrorEvent, **kwargs) -> None:
    logger.error(
        "telegram_update_failed",
        exception_type=type(exception.exception).__name__,
    )

    bot: Bot = kwargs["bot"]
    from_user: Optional[User] = kwargs.get("event_from_user", None)
    errors_messages: Errors = kwargs["errors"]

    if (
        isinstance(exception.exception, aiogram.exceptions.TelegramBadRequest)
        and from_user
    ):
        if "message is too long" in exception.exception.message.lower():
            await bot.send_message(
                chat_id=from_user.id,
                text=errors_messages.too_long_message_text,
            )

        elif "chat not found" in exception.exception.message.lower():
            await bot.send_message(
                chat_id=from_user.id,
                text=errors_messages.chat_not_found,
            )

    return


__all__ = ["errors_router"]
