import os

ROOT_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_FILE_PATH = os.path.join(ROOT_DIR, "config.yaml")


__all__ = ["CONFIG_FILE_PATH", "ROOT_DIR"]
