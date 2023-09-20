from aiogram import Bot
from sulguk import AiogramSulgukMiddleware

from src.config import BotConfig


def setup_bot(config: BotConfig) -> Bot:
    bot: Bot = Bot(
        token=config.token.get_secret_value(),
    )

    # https://github.com/Tishka17/sulguk#example-for-aiogram-users
    bot.session.middleware(AiogramSulgukMiddleware())

    return bot


__all__ = ["setup_bot"]
