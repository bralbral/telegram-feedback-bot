from aiogram import Bot
from aiogram import F
from aiogram import Router
from aiogram.types import ContentType
from aiogram.types import Message


router = Router(name="users")


@router.message(
    F.content_type
    in (
        ContentType.TEXT,
        ContentType.ANIMATION,
        ContentType.AUDIO,
        ContentType.DOCUMENT,
        ContentType.PHOTO,
        ContentType.VIDEO,
        ContentType.VOICE,
    )
)  # type: ignore
async def redirect_message(message: Message, bot: Bot, chat_id: int, **kwargs):
    if len(message.text) > 4096 or (message.caption and len(message.caption) > 1000):
        await message.reply("❌ Please send a smaller text message.")
        return

    if len(message.caption):
        await message.copy_to(
            chat_id,
            caption=((message.caption or "") + f"\n\n#id{message.from_user.id}"),
        )
    else:
        await bot.send_message(
            chat_id, message.html_text + f"\n\n#id{message.from_user.id}"
        )


@router.message()  # type: ignore
async def unsupported_types(message: Message, **kwargs):
    await message.reply(
        "❌ Unsupported message type. You can check available message types using /help command."
    )
