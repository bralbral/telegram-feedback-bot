from typing import Any

from aiogram.exceptions import TelegramBadRequest
from aiogram.types import ErrorEvent
from aiogram_dialog import DialogManager


async def on_unknown_intent(event: ErrorEvent, dialog_manager: DialogManager) -> Any:
    """Example of handling UnknownIntent Error and starting new dialog."""
    if event.update.callback_query:
        await event.update.callback_query.answer(
            "Bot process was restarted due to maintenance.\n" "Try again.",
        )
        try:
            await event.update.callback_query.message.delete()
        except TelegramBadRequest:
            pass  # whatever


__all__ = ["on_unknown_intent"]
