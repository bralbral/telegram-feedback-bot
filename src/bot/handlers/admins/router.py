from aiogram import Bot
from aiogram import F
from aiogram import Router
from aiogram.exceptions import TelegramAPIError
from aiogram.types import Message

from .utils import extract_id
from src.bot.filters import FilterByChatID

router = Router(name="admins")


@router.message(FilterByChatID(), F.reply_to_message)  # type: ignore
async def reply_to_user(message: Message, bot: Bot, **kwargs):
    try:
        user_id = extract_id(message.reply_to_message)
    except ValueError as ex:
        await message.reply(f"❌ Error during extract_id: {str(ex)}")
        return

    try:
        await bot.copy_message(
            from_chat_id=message.chat.id, chat_id=user_id, message_id=message.message_id
        )
    except TelegramAPIError as ex:
        await message.reply(f"❌ Error during copying: {str(ex)}")


__all__ = ["router"]
