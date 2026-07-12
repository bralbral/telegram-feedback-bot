import yaml

from .models import Config


def load_config(config_path: str) -> Config:
    """
    :param config_path:
    :return:
    """
    with open(file=config_path, mode="rb") as fh:
        raw_data = yaml.safe_load(fh)

    return Config.model_validate(raw_data)


__all__ = ["load_config"]
