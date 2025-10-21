import pytest
import yaml
from selenium.webdriver.support.events import EventFiringWebDriver
from utilities.driver_factory import get_driver
from utilities.webdriver_listeners import WebDriverListeners

@pytest.fixture(scope="class")
def setup(request):
    driver = get_driver()
    event_driver = EventFiringWebDriver(driver, WebDriverListeners())

    with open("config/config.yaml", "r") as f:
        config = yaml.safe_load(f)
    with open("config/credentials.yaml", "r") as f:
        creds = yaml.safe_load(f)

    base_url = config["base_url"]
    event_driver.get(base_url)

    request.cls.driver = event_driver
    request.cls.creds = creds
    yield
    event_driver.quit()
