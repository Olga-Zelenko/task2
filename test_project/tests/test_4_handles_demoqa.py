import pytest
from framework.logger.logger import BaseLogger
from test_project.pages.main_page import MainPage
from test_project.pages.alerts_windows_page import AlertsWindowsPage
from test_project.pages.sample_page import SamplePage
from test_project.pages.browser_windows_page import BrowserWindowsPage
from test_project.pages.links_page import LinksPage
from test_project.data.data_test import TestData


@pytest.mark.usefixtures("setup_and_close_browser")
class Test4Handles:
    def test_4_handles(self):
        BaseLogger.info(f"\nНачинаем выполнение теста {self.__class__.__name__}")
        main_page = MainPage()
        sample_page = SamplePage()
        alerts_windows_page = AlertsWindowsPage()
        browser_windows_page = BrowserWindowsPage()
        links_page = LinksPage()
        BaseLogger.info("Проверяем, что главная страница открылась")
        assert main_page.is_open_page(), "Главная страница не открылась"
        BaseLogger.info("Главная страница открылась")

        main_page.click_alerts_frame_btn()
        alerts_windows_page.left_menu.click_browser_windows_menu_item()
        BaseLogger.info("Проверяем, что страница с формой Browser windows открылась")
        assert (browser_windows_page.is_open_page()), "Страница с формой Browser windows не открылась"
        BaseLogger.info("Страница с формой Browser windows открылась")

        list_window_handles_before = browser_windows_page.window_handles()
        browser_windows_page.click_new_tab_btn()
        list_window_handles_after = browser_windows_page.window_handles()
        browser_windows_page.switch_to_window(list_window_handles_after[1])
        BaseLogger.info("Проверяем, что новая вкладка появилась")
        assert (len(list_window_handles_after) - len(list_window_handles_before) == TestData.NUMBER_FRAMES),\
            "Новая вкладка не появилась"
        BaseLogger.info("Новая вкладка появилась")
        BaseLogger.info(f"Проверяем, что новая вкладка имеет в url {TestData.URL_SAMPLE}")
        assert TestData.URL_SAMPLE == browser_windows_page.get_relative_link(), \
            f"Новая вкладка не имеет в url {TestData.URL_SAMPLE}"
        BaseLogger.info(f"Новая вкладка имеет в url {TestData.URL_SAMPLE}")
        BaseLogger.info("Проверяем, что страница Sample page открылась")
        assert sample_page.is_open_page(), "Страница Sample page не открылась"
        BaseLogger.info("Страница Sample page открылась")

        sample_page.close_current_window()
        browser_windows_page.switch_to_window(browser_windows_page.window_handles()[0])
        BaseLogger.info("Проверяем, что страница с формой Browser windows открылась")
        assert (browser_windows_page.is_open_page()), "Страница с формой Browser windows не открылась"
        BaseLogger.info("Страница с формой Browser windows открылась")

        browser_windows_page.left_menu.click_elements_menu()
        browser_windows_page.left_menu.wait_visibility_links_item()
        browser_windows_page.left_menu.click_links_menu_item()
        BaseLogger.info("Проверяем, что страница с формой Links открылась")
        assert links_page.is_open_page(), "Страница с формой Links не открылась"
        BaseLogger.info("Страница с формой Links открылась")

        list_window_handles_before = links_page.window_handles()
        links_page.click_home_link()
        list_window_handles_after = links_page.window_handles()
        links_page.switch_to_window(list_window_handles_after[1])
        BaseLogger.info("Проверяем, что новая вкладка появилась")
        assert (len(list_window_handles_after) - len(list_window_handles_before) == TestData.NUMBER_FRAMES),\
            "Новая вкладка не появилась"
        BaseLogger.info("Новая вкладка появилась")
        BaseLogger.info("Проверяем, что главная страница открылась")
        assert main_page.is_open_page(), "Главная страница не открылась"
        BaseLogger.info("Главная страница открылась")

        main_page.switch_to_window(list_window_handles_after[0])
        BaseLogger.info("Проверяем, что на первой вкладке открыта страница с формой Links")
        assert links_page.is_open_page(), "Страница с формой Links не открыта"
        BaseLogger.info("На первой вкладке открыта страница с формой Links")
        BaseLogger.info(f"\nЗавершаем выполнение теста {self.__class__.__name__}. Тест выполнен успешно.")
