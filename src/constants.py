import os

VERSION: str = "2024-05-31.19"
ROOT_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_FILE_PATH: str = os.path.join(ROOT_DIR, "config.yaml")


__all__ = ["CONFIG_FILE_PATH", "ROOT_DIR", "VERSION"]
