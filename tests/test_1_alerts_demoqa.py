from pages.main_page import MainPage
from pages.alerts_windows_page import AlertsWindowsPage
from utilities import random_str
from logger import logger
from data_test import TestData
from pages.alerts_page import AlertsPage


class Test1Alerts:

    def test_1_alerts(self):
        logger.info(f"\nНачинаем выполнение теста {self.__class__.__name__}")
        main_page = MainPage()
        alerts_page = AlertsPage()
        alerts_windows_page = AlertsWindowsPage()
        assert main_page.is_open_page(), "Главная страница не открылась"

        main_page.click_alerts_frame_btn()
        alerts_windows_page.left_menu.click_alerts_menu_item()
        assert alerts_page.is_open_page(), "Страница с формой Alerts не открылась"

        alerts_page.click_btn_to_see_alert()
        assert TestData.MESSAGE_BUTTON in alerts_page.getting_text_alert(), \
            "Алерт с текстом 'You clicked a button' не открылся"

        alerts_page.accept_alert()
        assert len(alerts_page.getting_list_frame()) == 1, "Alert не закрылся"

        alerts_page.click_btn_confirm_box()
        assert TestData.MESSAGE_CONFIRM_BOX in alerts_page.getting_text_alert(), \
            "Алерт с текстом 'Do you confirm action' не открылся"

        alerts_page.accept_alert()
        assert len(alerts_page.getting_list_frame()) == 1, "Alert не закрылся"
        assert TestData.MESSAGE_ALERT in alerts_page.getting_text_message_confirm_box(), \
            "Сообщение 'You selected Ok'не появилось"

        alerts_page.click_btn_prompt_box()
        assert TestData.MESSAGE_PROMPT_BOX in alerts_page.getting_text_alert(), \
            "Алерт с текстом 'Please enter your name' не открылся"

        alerts_page.send_keys_alert(random_str)
        alerts_page.accept_alert()
        assert len(alerts_page.getting_list_frame()) == 1, "Alert не закрылся"
        assert TestData.MESSAGE_SEND_KEYS_ALERT + random_str == alerts_page.getting_text_message_prompt_box(),\
            "Введённое в prompt box сообщение пользователем не появилось"
