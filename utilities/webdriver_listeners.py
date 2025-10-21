from selenium.webdriver.support.events import AbstractEventListener

class WebDriverListeners(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print(f"[BEFORE NAVIGATE] Navigating to {url}")

    def after_navigate_to(self, url, driver):
        print(f"[AFTER NAVIGATE] Navigated to {url}")

    def before_find(self, by, value, driver):
        print(f"[BEFORE FIND] Searching for element by {by} with value {value}")

    def after_find(self, by, value, driver):
        print(f"[AFTER FIND] Found element by {by} with value {value}")

    def before_click(self, element, driver):
        print(f"[BEFORE CLICK] Clicking on element {element}")

    def after_click(self, element, driver):
        print(f"[AFTER CLICK] Clicked on element {element}")
