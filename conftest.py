import logging
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from fixtures.pages.application import Application
from webdriver_auto_update import check_driver
logger = logging.getLogger("moodle")

check_driver()
def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://berpress.github.io/online-grocery-store/",
        help="Moodle url",
    ),
    parser.addoption(
        "--headless",
        action="store",
        default="false",
        help="enter 'true' if you want run tests in headless mode of browser,\n"
        "enter 'false' - if not",
    ),


@pytest.fixture()
def app(request):
    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    chrome_options = Options()
    if headless == "false":
        chrome_options.headless = False
    else:
        chrome_options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.set_window_size(1920, 1080)
    logger.info(f"Start app on {url}")
    app = Application(driver, url)
    yield app
    app.quit()

