import os
from pages.page_base import PageBase
from locators.login_locators import LoginLocators
from utilities.yaml_reader import YamlReader


class LoginPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        # Read credentials from YAML file
        creds_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", "credentials.yaml")
        self.creds = YamlReader.read_yaml(creds_path)
        self.username = self.creds.get("username")
        self.password = self.creds.get("password")

    def login(self):
        """Perform login using credentials from config file."""
        self.wait_for_visibility(LoginLocators.USERNAME_INPUT)
        self.send_keys(LoginLocators.USERNAME_INPUT, self.username)
        self.send_keys(LoginLocators.PASSWORD_INPUT, self.password)
        self.click(LoginLocators.LOGIN_BUTTON)
