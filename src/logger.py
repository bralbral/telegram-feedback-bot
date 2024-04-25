import logging
import sys
from typing import Any

import orjson
import structlog
from structlog.stdlib import BoundLogger
from structlog.typing import EventDict

from src.constants import VERSION


def add_version(
    logger: logging.Logger, method_name: str, event_dict: EventDict
) -> EventDict:
    event_dict["version"] = VERSION

    return event_dict


def setup_logging() -> None:
    log_level = logging.INFO

    structlog.configure(
        cache_logger_on_first_use=True,
        wrapper_class=structlog.make_filtering_bound_logger(log_level),
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            add_version,
            structlog.processors.format_exc_info,
            structlog.processors.TimeStamper(
                fmt="%Y-%m-%d %H:%M:%S UTC", utc=False, key="@timestamp"
            ),
            structlog.processors.JSONRenderer(serializer=orjson.dumps),
        ],
        logger_factory=structlog.BytesLoggerFactory(),
    )

    handler = logging.StreamHandler()
    # Use OUR `ProcessorFormatter` to format all `logging` entries.
    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    root_logger.setLevel(log_level)

    # disable aiogram loggers
    # https://github.com/aiogram/aiogram/blob/dev-3.x/aiogram/loggers.py

    for _logger_name in [
        "aiogram.dispatcher",
        "aiogram.event",
        "aiogram.middlewares",
        "aiogram.webhook",
        "aiogram.scene",
    ]:

        logging.getLogger(_logger_name).handlers.clear()
        logging.getLogger(_logger_name).propagate = False

    def handle_exception(exc_type: Any, exc_value: Any, exc_traceback: Any) -> None:
        """
        Log any uncaught exception instead of letting it be printed by Python
        (but leave KeyboardInterrupt untouched to allow users to Ctrl+C to stop)
        See https://stackoverflow.com/a/16993115/3641865
        """
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return

        root_logger.error(
            "Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback)
        )

    sys.excepthook = handle_exception


setup_logging()
logger: BoundLogger = structlog.stdlib.get_logger()

__all__ = ["logger", "setup_logging"]
