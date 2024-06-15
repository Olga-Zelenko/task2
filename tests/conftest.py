import pytest
from utilities import ParsingData
from browser_class import Browser


@pytest.fixture(autouse=True)
def setup_and_close_browser():
    Browser().maximize_window()
    Browser().get_page(ParsingData.url_main_page)
    yield Browser()
    Browser().close_browser()
