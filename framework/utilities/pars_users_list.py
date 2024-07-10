from framework.utilities.pars_users_yaml import ParsUsersYaml
from test_project.models.user_class import User


class ParsingUsers:

    users_list = ParsUsersYaml("test_project\\data\\users.yaml").parsing_users_yaml()

    @staticmethod
    def make_instances_cls_user() -> list[User]:
        """Обрабатывает данные из Users-списка"""
        data_of_users = []
        list_users = []
        for i in range(0, len(ParsingUsers.users_list)):

            for key, value in ParsingUsers.users_list[i].items():
                data_of_users.append(value)
            list_users.append(User(*data_of_users))
            data_of_users = []
        return list_users
