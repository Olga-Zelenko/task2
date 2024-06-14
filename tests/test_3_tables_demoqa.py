from pages.main_page import MainPage
from pages.elements_page import ElementsPage
from pages.web_tables_page import WebTablesPage
from utilities import get_list_value_elem_class
from logger import logger
from data_test import *
import pytest


class Test3Tables:
    @pytest.mark.parametrize("user", [user_1, user_2])
    def test_3_tables(self, user):
        logger.info(f"\nНачинаем выполнение теста {self.__class__.__name__}")
        main_page = MainPage()
        elements_page = ElementsPage()
        web_tables_page = WebTablesPage()
        assert main_page.is_open_page(), "Главная страница не открылась"

        main_page.click_elements_btn()
        elements_page.left_menu.click_web_tables_menu_item()
        assert web_tables_page.is_open_page(), "Страница с формой Web tables не открылась"

        web_tables_page.click_add_btn()
        web_tables_page.wait_visibility_registration_form()
        assert web_tables_page.is_displayed_registration_form(), "Форма регистрации не открылась"

        web_tables_page.send_first_name(user.first_name)
        web_tables_page.send_last_name(user.last_name)
        web_tables_page.send_email_name(user.email)
        web_tables_page.send_age(user.age)
        web_tables_page.send_salary(user.salary)
        web_tables_page.send_departament(user.departament)
        web_tables_page.submit_registration_form()
        web_tables_page.wait_invisibility_registration_form()
        assert TestData.CLASS_OPEN_REGISTRATION_FORM not in web_tables_page.get_attribute_class_body(), \
            "Форма регистрации не закрылась"

        list_text_table_cell = web_tables_page.getting_text_table_cell()
        assert all(x in list_text_table_cell for x in get_list_value_elem_class(user)), "User не добавлен в таблицу"

        count_str_before = web_tables_page.find_elements_delete_btn()
        web_tables_page.click_delete_latest_str()
        count_str_after = web_tables_page.find_elements_delete_btn()
        assert count_str_before != count_str_after, "Количество записей в таблице не изменилось"
        assert user.email not in web_tables_page.getting_text_table_cell(), "User не удалён из таблицы"
