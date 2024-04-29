from aiogram import Dispatcher

from .admins import router as admin_router
from .errors import errors_router
from .misc import router as misc_router
from .users import router as users_router


def register_handlers(dp: Dispatcher) -> None:
    dp.include_router(misc_router)
    dp.include_router(users_router)
    dp.include_router(admin_router)
    dp.include_router(errors_router)


__all__ = ["register_handlers"]
