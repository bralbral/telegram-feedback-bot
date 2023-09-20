import structlog
from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.state import State
from aiogram.types import Message

from src.bot.utils.help import send_help_message

logger = structlog.stdlib.get_logger()
router = Router(name="misc")


@router.message(
    Command("start", "help"),
    State(state="*"),
)  # type: ignore
async def start_help_handler(message: Message, **kwargs) -> None:
    await send_help_message(message=message)


__all__ = ["router"]
