# trans/config.py

from pathlib import Path
from configparser import ConfigParser
from trans import (
    __app_name__,
    exceptions
)
import typer

config_parser = ConfigParser()
class Config:
    DEFAULT_CONFIG_DIR_PATH = Path(typer.get_app_dir(__app_name__))
    DEFAULT_CONFIG_FILE_PATH = DEFAULT_CONFIG_DIR_PATH / "config.ini"
    def __init__(self, otpath : Path) -> None :
        self.otpath = otpath

    # create configuration file
    def create_config_file(self) -> bool :
        try :
            Config.DEFAULT_CONFIG_FILE_PATH.touch(exist_ok=True)
        except OSError :
            raise OSError(":( configuration file failed to make!")
        return True

    # create configuration folder
    def create_config_dir(self) -> bool :
        try :
            Config.DEFAULT_CONFIG_DIR_PATH.mkdir(exist_ok=True)
        except OSError :
            raise OSError(":( making configuration folder failed!")
        return True

    # writing inside configuration file
    def write(self, section : str, key : str, value : str) -> bool :
        config_parser.read(Config.DEFAULT_CONFIG_FILE_PATH)
        config_parser[section] = {key : value}
        try :
            with Config.DEFAULT_CONFIG_FILE_PATH.open("w") as config_file :
                config_parser.write(config_file)
        except exceptions.ConfigurationError :
            raise exceptions.ConfigurationError(":( assigning data to config file failed!")
        return True