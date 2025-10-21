from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as GeckoService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
import yaml

def read_config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)

def get_driver():
    config = read_config()
    browser = config["browser"]
    headless = config["headless"]

    if browser.lower() == "chrome":
        options = Options()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    elif browser.lower() == "firefox":
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(service=GeckoService(GeckoDriverManager().install()), options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.implicitly_wait(config["implicit_wait"])
    return driver
