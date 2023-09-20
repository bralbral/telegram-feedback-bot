from aiogram import Dispatcher

from .misc import router as misc_router


def register_handlers(dp: Dispatcher) -> None:
    # post must be upper due to process /post command
    dp.include_router(misc_router)


__all__ = ["register_handlers"]
