from framework.logger.logger import BaseLogger
from test_project.pages.main_page import MainPage
from test_project.pages.alerts_windows_page import AlertsWindowsPage
from framework.utilities.random_util import RandomStr
from test_project.data.data_test import TestData
from test_project.pages.alerts_page import AlertsPage
import pytest


@pytest.mark.usefixtures("setup_and_close_browser")
class Test1Alerts:
    def test_1_alerts(self):
        BaseLogger.info(f"\nНачинаем выполнение теста {self.__class__.__name__}")
        main_page = MainPage()
        alerts_page = AlertsPage()
        alerts_windows_page = AlertsWindowsPage()
        BaseLogger.info("Проверяем, что главная страница открылась")
        assert main_page.is_open_page(), "Главная страница не открылась"
        BaseLogger.info("Главная страница открылась")

        main_page.click_alerts_frame_btn()
        alerts_windows_page.left_menu.click_alerts_menu_item()
        BaseLogger.info("Проверяем, что страница с формой Alerts открылась")
        assert alerts_page.is_open_page(), "Страница с формой Alerts не открылась"
        BaseLogger.info("Страница с формой Alerts открылась")

        alerts_page.click_btn_to_see_alert()
        BaseLogger.info(f"Проверяем, что Алерт с текстом {TestData.MESSAGE_BUTTON} открылся")
        assert (TestData.MESSAGE_BUTTON in alerts_page.getting_text_alert()), \
            f"Алерт с текстом {TestData.MESSAGE_BUTTON} не открылся"
        BaseLogger.info(f"Алерт с текстом {TestData.MESSAGE_BUTTON} открылся")

        alerts_page.accept_alert()
        BaseLogger.info("Проверяем, что алерт закрылся")
        assert (len(alerts_page.getting_list_frame()) == TestData.NUMBER_FRAMES), "Alert не закрылся"
        BaseLogger.info("Алерт закрылся")

        alerts_page.click_btn_confirm_box()
        BaseLogger.info(f"Проверяем, что Алерт с текстом {TestData.MESSAGE_CONFIRM_BOX} открылся")
        assert (TestData.MESSAGE_CONFIRM_BOX in alerts_page.getting_text_alert()), \
            f"Алерт с текстом {TestData.MESSAGE_CONFIRM_BOX} не открылся"
        BaseLogger.info(f"Алерт с текстом {TestData.MESSAGE_CONFIRM_BOX} открылся")

        alerts_page.accept_alert()
        BaseLogger.info(f"Проверяем, что алерт закрылся и появилось сообщение {TestData.MESSAGE_ALERT}")
        assert (len(alerts_page.getting_list_frame()) == TestData.NUMBER_FRAMES), "Alert не закрылся"
        BaseLogger.info("Алерт закрылся")
        assert (TestData.MESSAGE_ALERT in alerts_page.getting_text_message_confirm_box()), \
            f"Сообщение {TestData.MESSAGE_ALERT} не появилось"
        BaseLogger.info(f"Сообщение {TestData.MESSAGE_ALERT} появилось")

        alerts_page.click_btn_prompt_box()
        BaseLogger.info(f"Проверяем, что Алерт с текстом {TestData.MESSAGE_PROMPT_BOX} открылся")
        assert (TestData.MESSAGE_PROMPT_BOX in alerts_page.getting_text_alert()), \
            f"Алерт с текстом {TestData.MESSAGE_PROMPT_BOX} не открылся"
        BaseLogger.info(f"Алерт с текстом {TestData.MESSAGE_PROMPT_BOX} открылся")

        random_str = RandomStr().generation_str()
        alerts_page.send_keys_alert(random_str)
        alerts_page.accept_alert()
        BaseLogger.info("Проверяем, что Алерт закрылся")
        assert (len(alerts_page.getting_list_frame()) == TestData.NUMBER_FRAMES), "Alert не закрылся"
        BaseLogger.info("Алерт закрылся")

        BaseLogger.info(f"Проверяем, что введённое в prompt box сообщение '{random_str}' пользователем появилось")
        assert (f"{TestData.MESSAGE_SEND_KEYS_ALERT}{random_str}" == alerts_page.getting_text_message_prompt_box()), \
            "Введённое в prompt box сообщение пользователем не появилось"
        BaseLogger.info(f"Введённое в prompt box сообщение '{random_str}' пользователем появилось")
        BaseLogger.info(f"\nЗавершаем выполнение теста {self.__class__.__name__}. Тест выполнен успешно.")
