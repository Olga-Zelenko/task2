from framework.logger.logger import BaseLogger
from test_project.pages.main_page import MainPage
from test_project.pages.elements_page import ElementsPage
from test_project.pages.web_tables_page import WebTablesPage
from framework.utilities.list_util import ListValueElement
from test_project.data.data_test import TestData
from framework.utilities.pars_users_list import ParsingUsers
import pytest


@pytest.mark.usefixtures("setup_and_close_browser")
class Test3Tables:
    @pytest.mark.parametrize("user", ParsingUsers.make_instances_cls_user())
    def test_3_tables(self, user):
        BaseLogger.info(f"\nНачинаем выполнение теста {self.__class__.__name__}")
        main_page = MainPage()
        elements_page = ElementsPage()
        web_tables_page = WebTablesPage()
        BaseLogger.info("Проверяем, что главная страница открылась")
        assert main_page.is_open_page(), "Главная страница не открылась"
        BaseLogger.info("Главная страница открылась")

        main_page.click_elements_btn()
        elements_page.left_menu.click_web_tables_menu_item()
        BaseLogger.info("Проверяем, что страница с формой Web tables открылась")
        assert (web_tables_page.is_open_page()), "Страница с формой Web tables не открылась"
        BaseLogger.info("Страница с формой Web tables открылась")

        web_tables_page.click_add_btn()
        web_tables_page.wait_visibility_registration_form()
        BaseLogger.info("Проверяем, что форма регистрации открылась")
        assert (web_tables_page.is_displayed_registration_form()), "Форма регистрации не открылась"
        BaseLogger.info("Форма регистрации открылась")

        web_tables_page.send_all_form(*ListValueElement.get_list_value_elem_class(user))
        web_tables_page.submit_registration_form()
        web_tables_page.wait_invisibility_registration_form()
        BaseLogger.info("Проверяем, что форма регистрации закрылась")
        assert (TestData.CLASS_OPEN_REGISTRATION_FORM not in web_tables_page.get_attribute_class_body()),\
            "Форма регистрации не закрылась"
        BaseLogger.info("Форма регистрации закрылась")

        list_text_table_cell = web_tables_page.getting_text_table_cell()
        BaseLogger.info("Проверяем, что User добавлен в таблицу")
        assert all(x in list_text_table_cell for x in ListValueElement.get_list_value_elem_class(user)),\
            "User не добавлен в таблицу"
        BaseLogger.info("User добавлен в таблицу")

        count_str_before = web_tables_page.find_elements_delete_btn()
        web_tables_page.click_delete_latest_str()
        count_str_after = web_tables_page.find_elements_delete_btn()
        BaseLogger.info("Проверяем, что количество записей в таблице изменилось")
        assert (count_str_before != count_str_after), "Количество записей в таблице не изменилось"
        BaseLogger.info("Количество записей в таблице изменилось")
        BaseLogger.info("Проверяем, что User удалён из таблицы")
        assert (user.email not in web_tables_page.getting_text_table_cell()), "User не удалён из таблицы"
        BaseLogger.info("User удалён из таблицы")
        BaseLogger.info(f"\nЗавершаем выполнение теста {self.__class__.__name__}. Тест выполнен успешно.")
