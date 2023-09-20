from aiogram import Bot
from aiogram import F
from aiogram import Router
from aiogram.enums import ContentType
from aiogram.types import Message
from sulguk import SULGUK_PARSE_MODE

router = Router(name="users")


# process messages only from PM
# with allowed content type
@router.message(
    F.chat.id == F.from_user.id,
    F.content_type.in_(
        {
            ContentType.TEXT,
            ContentType.ANIMATION,
            ContentType.AUDIO,
            ContentType.DOCUMENT,
            ContentType.PHOTO,
            ContentType.VIDEO,
            ContentType.VOICE,
        }
    ),
)  # type: ignore
async def handle_supported_type_message(
    message: Message,
    bot: Bot,
    chat_id: int,
    **kwargs,
):
    from_chat_id = message.from_user.id
    message_id = message.message_id

    if message.text:
        if len(message.text) > 4000:
            await message.reply("❌ Too long message text")
            return

        message_text = f"<br/>#id{message.from_user.id}<br/>" + message.html_text

        await bot.send_message(
            chat_id=chat_id, text=message_text, parse_mode=SULGUK_PARSE_MODE
        )

    else:
        caption = message.caption if message.caption else ""
        caption += f"<br/>#id{message.from_user.id}<br/>"

        await bot.copy_message(
            chat_id=chat_id,
            from_chat_id=from_chat_id,
            message_id=message_id,
            caption=caption,
            parse_mode=SULGUK_PARSE_MODE,
        )

    await message.reply(text="✅ Please wait for response.")

    return


# process messages only from PM
# with disallowed content type
@router.message(
    F.chat.id == F.from_user.id,
    ~F.content_type.in_(
        {
            ContentType.TEXT,
            ContentType.ANIMATION,
            ContentType.AUDIO,
            ContentType.DOCUMENT,
            ContentType.PHOTO,
            ContentType.VIDEO,
            ContentType.VOICE,
        }
    ),
)  # type: ignore
async def handle_unsupported_type_message(
    message: Message,
    **kwargs,
):
    await message.reply(
        text="❌ Unsupported message type.<br/>Please check <b>/help</b> command.",
        parse_mode=SULGUK_PARSE_MODE,
    )


__all__ = ["router"]
