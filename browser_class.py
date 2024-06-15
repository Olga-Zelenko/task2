from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utilities import ParsingData
from urllib.parse import urlparse

from browser_factory import FactoryBrowser
from singleton_object import SingletonWebDriver


class Browser(SingletonWebDriver):
    def __init__(self):
        self._driver = FactoryBrowser.create_browser()

    def maximize_window(self):
        return self._driver.maximize_window()

    def get_page(self, page):
        return self._driver.get(page)

    def find_element(self, by, locator):
        return self._driver.find_element(by, locator)

    def find_elements(self, by, locator):
        return self._driver.find_elements(by, locator)

    def close_page(self):
        return self._driver.close()

    def wait(self):
        return WebDriverWait(self._driver, ParsingData.timeout)

    def check_element_displayed(self, by, locator):
        self.wait().until(
            EC.presence_of_element_located((by, locator))
        )
        return self.find_element(by, locator).is_displayed()

    def get_current_url(self):
        return self._driver.current_url

    def switch_alert(self):
        """Переключение на alert"""
        return self._driver.switch_to.alert

    def switch_to_iframe(self, by, locator):
        element = self.find_element(by, locator)
        return self._driver.switch_to.frame(element)

    def getting_list_frame(self):
        return self._driver.window_handles

    def close_browser(self):
        SingletonWebDriver.clear_instance()
        self._driver.quit()

    def current_window_handle(self) -> str:
        window_handle = self._driver.current_window_handle
        return window_handle

    def window_handles(self) -> list[str]:
        window_handles = self._driver.window_handles
        return window_handles

    def switch_to_window(self, name_window):
        return self._driver.switch_to.window(name_window)

    def get_relative_link(self):
        url = urlparse(self._driver.get_current_url())
        relative_link = url.path
        return relative_link

    def close_current_window(self):
        self._driver.close()

    def check_new_window_open(self, action) -> bool:
        list_window_handles_before = self.window_handles()
        action()
        list_window_handles_after = self.window_handles()
        return len(list_window_handles_after) - len(list_window_handles_before) == 1


