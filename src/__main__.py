import asyncio
import os

import structlog
import uvloop
from aiogram import Bot
from aiogram import Dispatcher

from src.bot import setup_bot
from src.bot import setup_dispatcher
from src.config import Config
from src.config import load_config
from src.constants import ROOT_DIR

logger = structlog.stdlib.get_logger()


uvloop.install()


async def main() -> None:
    config: Config = load_config(config_path=os.path.join(ROOT_DIR, "config.yaml"))

    dp: Dispatcher = setup_dispatcher(logger=logger, chat_id=config.chat_id)
    bot: Bot = setup_bot(config=config.bot)

    await logger.ainfo("Starting bot")
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
