import pytest
from selene.support.shared import browser
from selenium import webdriver
from paths import TMP_DIR

@pytest.fixture(scope='function', autouse=True)
def driver_configuration():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": TMP_DIR,
        "download.prompt_for_download": False,
    }
    options.add_experimental_option('prefs', prefs)
    options.page_load_strategy = 'eager'

    browser.config.driver_options = options
    browser.config.base_url = 'https://www.online-convert.com/ru'
    yield
    browser.quit()
