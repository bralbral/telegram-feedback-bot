from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.memory import SimpleEventIsolation
from structlog.stdlib import BoundLogger

from src.bot.handlers import register_handlers
from src.bot.middlewares import LoggerMiddleware
from src.config import Errors
from src.config import Messages


def setup_dispatcher(
    logger: BoundLogger, chat_id: int, messages: Messages, errors: Errors
) -> Dispatcher:
    """
    :param logger:
    :param chat_id:
    :param messages:
    :param errors:
    :return:
    """
    dp: Dispatcher = Dispatcher(
        storage=MemoryStorage(),
        logger=logger,
        chat_id=chat_id,
        messages=messages,
        errors=errors,
        events_isolation=SimpleEventIsolation(),
    )
    dp.message.middleware(LoggerMiddleware(logger=logger))

    register_handlers(dp)

    return dp


__all__ = ["setup_dispatcher"]
