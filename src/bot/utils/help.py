from aiogram.types import Message


async def send_help_message(message: Message) -> None:
    await message.answer(
        "test",
        disable_web_page_preview=True,
    )


__all__ = ["send_help_message"]
