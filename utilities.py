import json
import string
import random
import os


class ParsConfig:
    def __init__(self, file_name: str = "config.json"):
        self.file_name = file_name

    def parsing_config(self) -> dict:
        """Извлекает информацию из config файла, преобразовывая её в тип dict"""
        root_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(root_dir, self.file_name)
        with open(config_path, "r") as config:
            config = json.load(config)
        return config


class ParsingData:
    """Обрабатывает данные из config-словаря"""

    data = ParsConfig("config.json").parsing_config()

    url_main_page = data["url_main_page"]
    timeout = data["timeout"]
    max_len_srt = data["max_len_srt"]
    chrome = data["chrome"]
    firefox = data["firefox"]


class RandomStr:

    len_str = random.randint(1, ParsingData.max_len_srt)

    @staticmethod
    def generation_str() -> str:
        """Генерирует рандомную строку рандомной длины с заданным максимальным значением длины строки
        из букв/цифр/знаков препинания"""
        return "".join(
            random.choices(
                string.ascii_letters + string.digits + string.punctuation + " ",
                k=RandomStr.len_str,
            )
        )


def get_list_value_elem_class(instance):
    return list(map(str, list(instance.__dict__.values())))



