from aiogram import Bot
from aiogram import F
from aiogram import Router
from aiogram.exceptions import TelegramAPIError
from aiogram.types import Message

from .utils import extract_id
from src.bot.filters import FilterByChatID
from src.config import Errors
from src.config import Messages

router = Router(name="admins")


@router.message(FilterByChatID(), F.reply_to_message)  # type: ignore
async def reply_to_user(
    message: Message, bot: Bot, messages: Messages, errors: Errors, **kwargs
):
    """
    Answer to user by reply from admin chat or group
    :param message:
    :param bot:
    :param messages:
    :param errors:
    :param kwargs:
    :return:
    """
    try:
        user_id = extract_id(message.reply_to_message)
    except ValueError as ex:
        await message.reply(text=f"{errors.extract_user_id} {str(ex)}")
        return

    try:
        await bot.copy_message(
            from_chat_id=message.chat.id, chat_id=user_id, message_id=message.message_id
        )
        await message.reply(text=messages.notify_admin_about_success_answer)

    except TelegramAPIError as ex:
        await message.reply(text=f"{errors.copy_message} {str(ex)}")


__all__ = ["router"]
