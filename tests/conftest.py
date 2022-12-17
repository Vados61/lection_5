import pytest
from selene.support.shared import browser


@pytest.fixture(scope='session', autouse=True)
def create_config():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.base_url = 'https://demoqa.com'
    browser.config.hold_browser_open = True
    browser.open('/automation-practice-form')
    yield
    browser.quit()
