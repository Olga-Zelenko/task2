from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from framework.browser.browser import Browser


class BasePage(object):
    def __init__(self, locator_uniq_el: str, name_uniq_el: str):
        self.by = By.XPATH
        self.locator_uniq_el = locator_uniq_el
        self.name_uniq_el = name_uniq_el

    def is_open_page(self) -> bool:
        """Проверяет, открыта ли нужная страница путём определения присутствия на странице уникального для неё
        веб-элемента"""
        Browser().wait().until(EC.presence_of_element_located((self.by, self.locator_uniq_el)))
        return Browser().get_driver().find_element(self.by, self.locator_uniq_el).is_displayed()
