from framework.logger.logger import BaseLogger
from test_project.pages.main_page import MainPage
from test_project.pages.alerts_windows_page import AlertsWindowsPage
from test_project.pages.nested_frames_page import NestedFramesPage
from test_project.pages.frames_page import FramesPage
from test_project.data.data_test import TestData
import pytest


@pytest.mark.usefixtures("setup_and_close_browser")
class Test2Iframe:
    def test_2_iframe(self):
        BaseLogger.info(f"\nНачинаем выполнение теста {self.__class__.__name__}")
        main_page = MainPage()
        alerts_windows_page = AlertsWindowsPage()
        nested_frames_page = NestedFramesPage()
        frames_page = FramesPage()
        BaseLogger.info("Проверяем, что главная страница открылась")
        assert main_page.is_open_page(), "Главная страница не открылась"
        BaseLogger.info("Главная страница открылась")

        main_page.click_alerts_frame_btn()
        alerts_windows_page.left_menu.click_nested_frames_menu_item()
        BaseLogger.info("Проверяем, что страница с формой Nested frame открылась")
        assert (nested_frames_page.is_open_page()), "Страница с формой Nested frame не открылась"
        BaseLogger.info("Страница с формой Nested frame открылась")

        nested_frames_page.switch_iframe1_parent()
        BaseLogger.info(f"Проверяем, что в центре страницы есть надпись {TestData.TEXT_IFRAME1_PARENT}")
        assert (TestData.TEXT_IFRAME1_PARENT in nested_frames_page.getting_text_iframe1_parent()), \
            f"В центре страницы нет надписи {TestData.TEXT_IFRAME1_PARENT}"
        BaseLogger.info(f"В центре страницы есть надпись {TestData.TEXT_IFRAME1_PARENT}")

        nested_frames_page.switch_iframe_child()
        BaseLogger.info(f"Проверяем, что в центре страницы есть надпись {TestData.TEXT_IFRAME_CHILD}")
        assert (TestData.TEXT_IFRAME_CHILD in nested_frames_page.getting_text_iframe_child()), \
            f"В центре страницы нет надписи {TestData.TEXT_IFRAME_CHILD}"
        BaseLogger.info(f"В центре страницы есть надпись {TestData.TEXT_IFRAME_CHILD}")

        for i in range(TestData.NUMBER_LEVEL_FRAMES):
            nested_frames_page.switch_parent_frame()
        nested_frames_page.left_menu.click_frames_menu_item()
        BaseLogger.info("Проверяем, что страница с формой Frame открылась")
        assert frames_page.is_open_page(), "Страница с формой Frame не открылась"
        BaseLogger.info("Страница с формой Frame открылась")

        frames_page.switch_iframe_1()
        text_iframe_1 = frames_page.getting_text_iframe()
        frames_page.switch_parent_frame()
        frames_page.switch_iframe_2()
        text_iframe_2 = frames_page.getting_text_iframe()
        BaseLogger.info("Проверяем, что текст в Iframe1 совпадает с Iframe 2")
        assert text_iframe_1 == text_iframe_2, "Текст в Iframe1 не совпадает с Iframe 2"
        BaseLogger.info("Текст в Iframe1 совпадает с Iframe 2")
        BaseLogger.info(f"\nЗавершаем выполнение теста {self.__class__.__name__}. Тест выполнен успешно.")
