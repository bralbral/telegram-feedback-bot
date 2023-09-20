import yaml

from .models import Config


def load_config(config_path: str) -> Config:
    with open(file=config_path, mode="rb") as fh:
        raw_data: dict = yaml.load(stream=fh, Loader=yaml.FullLoader)
        config: Config = Config.model_validate(raw_data)
        return config


__all__ = ["load_config"]
