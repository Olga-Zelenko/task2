import pytest

from browser_class import Browser


@pytest.fixture
def browser():
    browser = Browser(browser_name="Chrome")
    browser.maximize_window()
    yield browser
    browser.close_browser()
