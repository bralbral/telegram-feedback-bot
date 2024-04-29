from aiogram import Bot
from aiogram import F
from aiogram import Router
from aiogram.enums import ContentType
from aiogram.types import Message

from .utils import extract_userinfo_from_message
from src.config import Errors
from src.config import Messages

router = Router(name="users")


@router.message(F.chat.id == F.from_user.id)  # type: ignore
async def handle_user_message(
    message: Message,
    bot: Bot,
    chat_id: int,
    messages: Messages,
    errors: Errors,
    **kwargs,
):
    """Handle user message and send it to admin chat (group)
    :param message:
    :param bot:
    :param chat_id:
    :param messages:
    :param errors:
    :param kwargs:
    :return:
    """
    if message.content_type not in (
        ContentType.TEXT,
        ContentType.ANIMATION,
        ContentType.AUDIO,
        ContentType.DOCUMENT,
        ContentType.PHOTO,
        ContentType.VIDEO,
        ContentType.VOICE,
    ):
        await message.reply(
            text=errors.unsupported_type,
        )

        return

    from_chat_id = message.from_user.id
    message_id = message.message_id

    if message.text:
        if len(message.text) > 3500:
            await message.reply(text=errors.too_long_message_text)
            return

        message_text = extract_userinfo_from_message(message) + message.html_text

        await bot.send_message(chat_id=chat_id, text=message_text)

    else:
        if message.caption and len(message.caption) > 1000:
            await message.reply(text=errors.too_long_message_caption)
            return

        caption = message.caption if message.caption else ""
        caption = extract_userinfo_from_message(message) + caption

        await bot.copy_message(
            chat_id=chat_id,
            from_chat_id=from_chat_id,
            message_id=message_id,
            caption=caption,
        )

    await message.reply(text=messages.notify_user_about_success_deliver)

    return


__all__ = ["router"]
