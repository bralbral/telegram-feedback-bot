from typing import Optional

import aiogram.exceptions
from aiogram import Bot
from aiogram import Router
from aiogram.types import User
from aiogram.types.error_event import ErrorEvent

from src.config import Errors

errors_router = Router(name="errors")


@errors_router.errors()  # type: ignore
async def error_handler(exception: ErrorEvent, **kwargs) -> None:

    bot: Bot = kwargs["bot"]
    from_user: Optional[User] = kwargs.get("event_from_user", None)
    errors_messages: Errors = kwargs["errors"]

    if (
        isinstance(exception.exception, aiogram.exceptions.TelegramBadRequest)
        and from_user
    ):
        if exception.exception.message.find("Bad Request: message is too long") > -1:
            await bot.send_message(
                chat_id=from_user.id,
                text=errors_messages.too_long_message_text,
            )

        elif exception.exception.message.find("Bad Request: chat not found") > -1:
            await bot.send_message(
                chat_id=from_user.id,
                text=errors_messages.chat_not_found,
            )

    return


__all__ = ["errors_router"]
