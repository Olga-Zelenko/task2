from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from browser_class import Browser
from urllib.parse import urlparse


class BasePage(object):
    def __init__(self, locator_uniq_el: str, name_uniq_el: str):
        self.locator_uniq_el = locator_uniq_el
        self.name_uniq_el = name_uniq_el
        self.by = By.XPATH

    def is_open_page(self) -> bool:
        Browser().wait().until(
            EC.presence_of_element_located((self.by, self.locator_uniq_el))
        )
        return Browser().find_element(self.by, self.locator_uniq_el).is_displayed()

    def get_relative_link(self):
        url = urlparse(Browser().get_current_url())
        relative_link = url.path
        return relative_link
