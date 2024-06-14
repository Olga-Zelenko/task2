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
        with open(config_path, 'r') as config:
            config = json.load(config)
        return config


class ParsingData:
    """Обрабатывает данные из config-словаря"""
    def __init__(self, data: dict):
        self.data = data

    def url_main_page(self):
        return self.data['url_main_page']

    def timeout(self):
        return self.data['timeout']

    def language_browser(self):
        return self.data['language_browser']

    def mode_browser(self):
        return self.data['mode_browser']

    def max_len_srt(self):
        return self.data['max_len_srt']

    def browser(self):
        return self.data['browser']


class RandomStr:
    def __init__(self, max_len_str: int):
        self.len_str = random.randint(1, max_len_str)

    def generation_str(self) -> str:
        """Генерирует рандомную строку рандомной длины с заданным максимальным значением длины строки
        из букв/цифр/знаков препинания"""
        return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation + " ", k=self.len_str))


def get_list_value_elem_class(instance):
    return list(map(str, list(instance.__dict__.values())))


config_dict = ParsConfig("config.json").parsing_config()
settings = ParsingData(config_dict)
random_str = RandomStr(settings.max_len_srt()).generation_str()
