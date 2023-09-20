from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.memory import SimpleEventIsolation
from structlog.stdlib import BoundLogger

from src.bot.handlers import register_handlers
from src.bot.middlewares import LoggerMiddleware


def setup_dispatcher(logger: BoundLogger, chat_id: int) -> Dispatcher:
    dp: Dispatcher = Dispatcher(
        storage=MemoryStorage(),
        logger=logger,
        chat_id=chat_id,
        events_isolation=SimpleEventIsolation(),
    )
    dp.message.middleware(LoggerMiddleware(logger=logger))

    register_handlers(dp)

    return dp


__all__ = ["setup_dispatcher"]
