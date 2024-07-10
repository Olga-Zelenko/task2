from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from test_project.data.pars_data_dict import ParsingData
from framework.browser.browser_factory import FactoryBrowser
from framework.singleton.singleton import Singleton
from urllib.parse import urlparse


class Browser(metaclass=Singleton):
    def __init__(self):
        self.__driver = None

    def get_driver(self):
        return self.__driver

    def setup_driver(self):
        self.__driver = FactoryBrowser.create_browser()

    def maximize_window(self) -> None:
        return self.get_driver().maximize_window()

    def go_to_page(self, page: str) -> None:
        return self.get_driver().get(page)

    @staticmethod
    def get_browser():
        return Browser()

    def wait(self) -> WebDriverWait:
        return WebDriverWait(self.get_driver(), ParsingData.TIMEOUT)

    def get_current_url(self) -> str:
        return self.get_driver().current_url

    def switch_alert(self) -> Alert:
        return self.get_driver().switch_to.alert

    def switch_to_iframe(self, element: WebElement) -> None:
        return self.get_driver().switch_to.frame(element)

    def current_window_handle(self) -> str:
        return self.get_driver().current_window_handle

    def window_handles(self) -> list[str]:
        return self.get_driver().window_handles

    def switch_to_window(self, name_window: str) -> None:
        return self.get_driver().switch_to.window(name_window)

    def switch_parent_frame(self) -> None:
        return self.get_driver().switch_to.parent_frame()

    def close_current_window(self):
        self.get_driver().close()

    def close_browser(self):
        self.get_driver().quit()
        Browser.clear_instance()

    def get_relative_link(self) -> str:
        url = urlparse(self.get_current_url())
        relative_link = url.path
        return relative_link
