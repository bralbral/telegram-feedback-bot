import asyncio
import platform

from aiogram import Bot, Dispatcher

from src.bot import setup_bot, setup_dispatcher
from src.config import Config, load_config
from src.constants import CONFIG_FILE_PATH, VERSION
from src.logger import logger

if platform.system() == "linux":
    import uvloop

    uvloop.install()


async def main() -> None:
    config: Config = load_config(config_path=CONFIG_FILE_PATH)
    dp: Dispatcher = setup_dispatcher(
        logger=logger,
        chat_id=config.chat_id,
        messages=config.messages,
        errors=config.errors,
    )
    bot: Bot = await setup_bot(config=config.bot)
    try:
        bot_info = await bot.get_me()
        logger.info("bot_starting", username=bot_info.username, version=VERSION)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped")
