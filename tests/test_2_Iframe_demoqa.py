from pages.main_page import MainPage
from pages.alerts_windows_page import AlertsWindowsPage
from pages.nested_frames_page import NestedFramesPage
from pages.frames_page import FramesPage
from logger import logger
from data_test import TestData


class Test2Iframe:
    def test_2_iframe(self):
        logger.info(f"\nНачинаем выполнение теста {self.__class__.__name__}")
        main_page = MainPage()
        alerts_windows_page = AlertsWindowsPage()
        nested_frames_page = NestedFramesPage()
        frames_page = FramesPage()
        assert main_page.is_open_page(), "Главная страница не открылась"

        main_page.click_alerts_frame_btn()
        alerts_windows_page.left_menu.click_nested_frames_menu_item()
        assert nested_frames_page.is_open_page(), "Страница с формой Nested frame не открылась"

        nested_frames_page.switch_iframe1_parent()
        assert TestData.TEXT_IFRAME1_PARENT in nested_frames_page.getting_text_iframe1_parent(), \
            f"В центре страницы нет надписи {TestData.TEXT_IFRAME1_PARENT}"

        nested_frames_page.switch_iframe_child()
        assert TestData.TEXT_IFRAME_CHILD in nested_frames_page.getting_text_iframe_child(), \
            f"В центре страницы нет надписи {TestData.TEXT_IFRAME_CHILD}"

        nested_frames_page.switch_parent_frame()
        nested_frames_page.switch_parent_frame()
        nested_frames_page.left_menu.click_frames_menu_item()
        assert frames_page.is_open_page(), "Страница с формой Frame не отокрылась"

        frames_page.switch_iframe_1()
        text_iframe_1 = frames_page.getting_text_iframe_1()
        frames_page.switch_parent_frame()
        frames_page.switch_iframe_2()
        text_iframe_2 = frames_page.getting_text_iframe_1()
        assert text_iframe_1 == text_iframe_2, "Текст в Iframe1 не совпадает с Iframe 2"
