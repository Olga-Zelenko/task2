from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from browser_factory import FactoryBrowser
from singleton_object import SingletonWebDriver


class Browser(SingletonWebDriver):
    def __init__(self, browser_name):
        self._driver = FactoryBrowser.create_browser(browser_name=browser_name)

    def maximize_window(self):
        return self._driver.maximize_window()

    def get_page(self, page):
        return self._driver.get(page)

    def close_page(self):
        return self._driver.close()

    def check_element_displayed(self, locator):
        WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
        return self._driver.find_element(By.XPATH, locator).is_displayed()

    def get_current_url(self):
        return self._driver.current_url

    def alert(self):
        """Переключение на alert"""
        return self._driver.switch_to.alert

    def switch_to_iframe(self, locator):
        element = self.check_element_displayed(locator)
        return self._driver.switch_to.frame(element)

    def windows_list(self):
        return self._driver.window_handles

    def close_browser(self):
        SingletonWebDriver.clear_instance()
        self._driver.quit()
