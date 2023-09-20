from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from structlog.stdlib import BoundLogger

from src.bot.handlers import register_handlers
from src.bot.middlewares import LoggerMiddleware


def setup_dispatcher(logger: BoundLogger) -> Dispatcher:
    dp: Dispatcher = Dispatcher(storage=MemoryStorage(), logger=logger)

    dp.message.middleware(LoggerMiddleware(logger=logger))

    register_handlers(dp)

    return dp


__all__ = ["setup_dispatcher"]
