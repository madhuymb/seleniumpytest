from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class PageBase:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.actions = ActionChains(driver)

    # ========== ELEMENT LOCATING METHODS ==========
    def find(self, locator):
        """Wait until element is present and return it."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def finds(self, locator):
        """Wait until multiple elements are present."""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    # ========== BASIC ELEMENT INTERACTIONS ==========
    def click(self, locator):
        """Wait until element is clickable and click."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator, value, clear_first=True):
        """Wait until element is visible and send keys."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        if clear_first:
            element.clear()
        element.send_keys(value)

    def get_text(self, locator):
        """Get visible text of an element."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text.strip()

    def get_attribute(self, locator, attribute):
        """Get an element’s attribute value."""
        element = self.find(locator)
        return element.get_attribute(attribute)

    # ========== WAIT UTILITIES ==========
    def wait_for_visibility(self, locator, timeout=10):
        """Wait until element is visible."""
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator, timeout=10):
        """Wait until element is clickable."""
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_for_presence(self, locator, timeout=10):
        """Wait until element is present in DOM (not necessarily visible)."""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def wait_for_invisibility(self, locator, timeout=10):
        """Wait until element disappears."""
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    # ========== VALIDATION HELPERS ==========
    def is_element_displayed(self, locator):
        """Return True if element is displayed."""
        try:
            return self.driver.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return False

    def is_element_present(self, locator):
        """Return True if element exists in DOM."""
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    # ========== ADVANCED ACTIONS ==========
    def move_to_element(self, locator):
        """Move the mouse to an element."""
        element = self.find(locator)
        self.actions.move_to_element(element).perform()

    def double_click(self, locator):
        """Double click on an element."""
        element = self.find(locator)
        self.actions.double_click(element).perform()

    def right_click(self, locator):
        """Right-click (context click) on an element."""
        element = self.find(locator)
        self.actions.context_click(element).perform()

    def drag_and_drop(self, source_locator, target_locator):
        """Drag one element and drop it onto another."""
        source = self.find(source_locator)
        target = self.find(target_locator)
        self.actions.drag_and_drop(source, target).perform()

    # ========== WINDOW & FRAME HANDLING ==========
    def switch_to_frame(self, locator):
        """Switch into an iframe."""
        frame = self.wait.until(EC.frame_to_be_available_and_switch_to_it(locator))
        return frame

    def switch_to_default_content(self):
        """Switch back to the main document."""
        self.driver.switch_to.default_content()

    def switch_to_window(self, index=0):
        """Switch to window/tab by index."""
        handles = self.driver.window_handles
        if index < len(handles):
            self.driver.switch_to.window(handles[index])
        else:
            raise IndexError(f"No window found at index {index}")

    def get_current_window_title(self):
        """Return current window title."""
        return self.driver.title

    # ========== NAVIGATION ==========
    def navigate(self, url):
        """Navigate to a specific URL."""
        self.driver.get(url)

    def refresh_page(self):
        """Refresh the current page."""
        self.driver.refresh()

    def back(self):
        """Navigate back in browser history."""
        self.driver.back()

    def forward(self):
        """Navigate forward in browser history."""
        self.driver.forward()

    # ========== ALERT HANDLING ==========
    def accept_alert(self):
        """Accept a browser alert."""
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            self.driver.switch_to.alert.accept()
        except TimeoutException:
            print("No alert to accept")

    def dismiss_alert(self):
        """Dismiss a browser alert."""
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            self.driver.switch_to.alert.dismiss()
        except TimeoutException:
            print("No alert to dismiss")

    def get_alert_text(self):
        """Get text from alert popup."""
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            return self.driver.switch_to.alert.text
        except TimeoutException:
            return None
