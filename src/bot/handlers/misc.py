import structlog
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from sulguk import SULGUK_PARSE_MODE

from src.constants import START_MESSAGE

logger = structlog.stdlib.get_logger()
router = Router(name="misc")


@router.message(
    Command("start", "help"),
)  # type: ignore
async def start_help_handler(message: Message, **kwargs) -> None:
    await message.answer(
        START_MESSAGE, disable_web_page_preview=True, parse_mode=SULGUK_PARSE_MODE
    )


__all__ = ["router"]
