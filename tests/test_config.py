import pytest
from pydantic import ValidationError

from src.config.models import Config


def test_config_rejects_unknown_fields() -> None:
    with pytest.raises(ValidationError):
        Config.model_validate(
            {
                "bot": {"token": "token"},
                "chat_id": -1001,
                "chatid": -1002,
            }
        )
