from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from browser_class import Browser
from selenium.webdriver.common.alert import Alert
from logger import logger
from urllib.parse import urlparse

driver = Browser()



class BasePage(object):
    def __init__(self, locator_uniq_el: str, name_uniq_el: str):
        self.locator_uniq_el = locator_uniq_el
        self.name_uniq_el = name_uniq_el
        self.by = By.XPATH

    def is_open_page(self) -> bool:
        return driver.check_element_displayed(self.by, self.locator_uniq_el)


