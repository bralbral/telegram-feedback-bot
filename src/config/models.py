from pydantic import SecretStr
from pydantic_settings import BaseSettings


class BotConfig(BaseSettings):
    """
    Bot config
    """

    token: SecretStr


class Config(BaseSettings):
    """
    All in one config
    """

    bot: BotConfig
    chat_id: int


__all__ = ["BotConfig", "Config"]
