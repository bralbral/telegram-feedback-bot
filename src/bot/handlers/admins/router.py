from typing import Optional

from aiogram import Bot, F, Router
from aiogram.exceptions import TelegramAPIError
from aiogram.types import Message

from src.bot.filters import FilterByChatID
from src.config import Errors, Messages

from .utils import extract_id

router = Router(name="admins")


@router.message(FilterByChatID(), F.reply_to_message)  # type: ignore
async def reply_to_user(
    message: Message,
    bot: Bot,
    messages: Messages,
    errors: Errors,
    **kwargs,
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

    if message.reply_to_message is None:
        return

    try:
        user_id = extract_id(message.reply_to_message, id_type="chat_id")
    except ValueError as ex:
        await message.reply(text=f"{errors.extract_user_id} {str(ex)}")
        return

    message_id: Optional[int] = None
    try:
        message_id = extract_id(message.reply_to_message, id_type="message_id")
    except ValueError:
        pass

    try:
        try:
            await bot.copy_message(
                from_chat_id=message.chat.id,
                chat_id=user_id,
                message_id=message.message_id,
                reply_to_message_id=message_id,
            )
        except TelegramAPIError as inner_ex:
            # message to reply can be deleted
            if not inner_ex.message.find("message to reply not found") > -1:
                raise inner_ex

            # try to resend message
            await bot.copy_message(
                from_chat_id=message.chat.id,
                chat_id=user_id,
                message_id=message.message_id,
            )

    except TelegramAPIError as ex:
        await message.reply(text=f"{errors.copy_message} {str(ex)}")
        return

    await message.reply(text=messages.notify_admin_about_success_answer)


__all__ = ["router"]
