from selenium.webdriver.support.wait import WebDriverWait
from utilities import ParsingData


from browser_factory import FactoryBrowser
from singleton_object import Singleton


class Browser(Singleton):
    __driver = FactoryBrowser.create_browser()

    def maximize_window(self):
        return self.__driver.maximize_window()

    def get_page(self, page):
        return self.__driver.get(page)

    def find_element(self, by, locator):
        return self.__driver.find_element(by, locator)

    def find_elements(self, by, locator):
        return self.__driver.find_elements(by, locator)

    def close_page(self):
        return self.__driver.close()

    def wait(self):
        return WebDriverWait(self.__driver, ParsingData.timeout)

    def get_current_url(self):
        return self.__driver.current_url

    def switch_alert(self):
        return self.__driver.switch_to.alert

    def switch_to_iframe(self, element):
        return self.__driver.switch_to.frame(element)

    def getting_list_frame(self):
        return self.__driver.window_handles

    def close_browser(self):
        self.__driver.quit()
        Browser.clear_instance()

    def current_window_handle(self) -> str:
        return self.__driver.current_window_handle

    def window_handles(self) -> list[str]:
        return self.__driver.window_handles

    def switch_to_window(self, name_window):
        return self.__driver.switch_to.window(name_window)

    def switch_parent_frame(self) -> None:
        return self.__driver.switch_to.parent_frame()

    def close_current_window(self):
        self.__driver.close()

    def check_new_window_open(self, action) -> bool:
        list_window_handles_before = self.window_handles()
        action()
        list_window_handles_after = self.window_handles()
        return len(list_window_handles_after) - len(list_window_handles_before) == 1
