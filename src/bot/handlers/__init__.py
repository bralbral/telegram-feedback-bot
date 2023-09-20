from aiogram import Dispatcher

from .misc import router as misc_router
from .users import router as users_router


def register_handlers(dp: Dispatcher) -> None:
    dp.include_router(misc_router)
    dp.include_router(users_router)


__all__ = ["register_handlers"]
