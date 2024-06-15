from pages.main_page import MainPage
from pages.alerts_windows_page import AlertsWindowsPage
from pages.sample_page import SamplePage
from pages.browser_windows_page import BrowserWindowsPage
from pages.links_page import LinksPage
from logger import logger
from data_test import *


class Test4Handles:
    def test_4_handles(self):
        logger.info(f"\nНачинаем выполнение теста {self.__class__.__name__}")
        main_page = MainPage()
        sample_page = SamplePage()
        alerts_windows_page = AlertsWindowsPage()
        browser_windows_page = BrowserWindowsPage()
        links_page = LinksPage()

        assert main_page.is_open_page(), "Главная страница не открылась"

        main_page.click_alerts_frame_btn()
        alerts_windows_page.left_menu.click_browser_windows_menu_item()
        assert (
            browser_windows_page.is_open_page()
        ), "Страница с формой Browser windows не открылась"

        list_window_handles_before = browser_windows_page.window_handles()
        browser_windows_page.click_new_tab_btn()
        list_window_handles_after = browser_windows_page.window_handles()
        browser_windows_page.switch_to_window(list_window_handles_after[1])
        assert (
            len(list_window_handles_after) - len(list_window_handles_before) == 1
        ), "Новая вкладка не появилась"
        assert TestData.URL_SAMPLE == browser_windows_page.get_relative_link(), (
            f"Новая вкладка не имеет в url " f"{TestData.URL_SAMPLE}"
        )
        assert sample_page.is_open_page(), "Страница Sample page не открылась"

        sample_page.close_current_window()
        browser_windows_page.switch_to_window(alerts_windows_page.window_handles()[0])
        assert (
            browser_windows_page.is_open_page()
        ), "Страница с формой Browser windows не открылась"

        browser_windows_page.left_menu.click_elements_menu()
        browser_windows_page.left_menu.wait_visibility_links_item()
        browser_windows_page.left_menu.click_links_menu_item()
        assert links_page.is_open_page(), "Страница с формой Links не открылась"

        list_window_handles_before = links_page.window_handles()
        links_page.click_home_link()
        list_window_handles_after = links_page.window_handles()
        links_page.switch_to_window(list_window_handles_after[1])
        assert (
            len(list_window_handles_after) - len(list_window_handles_before) == 1
        ), "Новая вкладка не появилась"
        assert main_page.is_open_page(), "Главная страница не открылась"

        main_page.switch_to_window(list_window_handles_after[0])
        assert links_page.is_open_page(), "Страница с формой Links не открылась"
