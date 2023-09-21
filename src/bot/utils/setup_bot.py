from aiogram import Bot
from aiogram.types import BotCommand
from aiogram.types import BotCommandScopeDefault
from sulguk import AiogramSulgukMiddleware

from src.config import BotConfig


async def setup_bot(config: BotConfig) -> Bot:
    bot: Bot = Bot(
        token=config.token.get_secret_value(),
    )

    # https://github.com/Tishka17/sulguk#example-for-aiogram-users
    bot.session.middleware(AiogramSulgukMiddleware())

    user_commands = [
        BotCommand(command="help", description="How to use bot"),
    ]

    await bot.set_my_commands(user_commands, scope=BotCommandScopeDefault())

    return bot


__all__ = ["setup_bot"]
