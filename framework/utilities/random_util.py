import string
import random
from test_project.data.pars_data_dict import ParsingData


class RandomStr:
    len_str = random.randint(1, ParsingData.MAX_LEN_SRT)

    @staticmethod
    def generation_str() -> str:
        """Генерирует рандомную строку рандомной длины с заданным максимальным значением длины строки
        из букв/цифр/знаков препинания"""
        return "".join(random.choices(string.ascii_letters + string.digits + string.punctuation + " ",
                                      k=RandomStr.len_str))
