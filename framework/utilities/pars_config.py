import json
import os


class ParsConfig:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def parsing_config(self) -> dict:
        """Извлекает информацию из config файла, преобразовывая её в тип dict"""
        root_dir = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )
        config_path = os.path.join(root_dir, self.file_name)
        with open(config_path, "r") as config:
            config = json.load(config)
        return config
