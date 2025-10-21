from time import sleep

import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.login()  # It will use credentials from YAML and login automatically
        sleep(2)
        login_page.validation()
