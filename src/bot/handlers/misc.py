import structlog
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from sulguk import SULGUK_PARSE_MODE

from src.config import Messages

logger = structlog.stdlib.get_logger()
router = Router(name="misc")


@router.message(
    Command("start", "help"),
)  # type: ignore
async def start_help_handler(message: Message, messages: Messages, **kwargs) -> None:
    """
    Handle /start or /help message
    :param message:
    :param messages:
    :param kwargs:
    :return:
    """
    await message.answer(
        messages.help_message,
        disable_web_page_preview=True,
        parse_mode=SULGUK_PARSE_MODE,
    )


__all__ = ["router"]
