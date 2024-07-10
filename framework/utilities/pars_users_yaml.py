import yaml
import os


class ParsUsersYaml:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def parsing_users_yaml(self) -> list:
        """Извлекает информацию из yaml файла, преобразовывая её в тип список словарей"""
        root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        users_path = os.path.join(root_dir, self.file_name)
        with open(users_path) as users:
            users = yaml.load(users, Loader=yaml.FullLoader)
        return users
