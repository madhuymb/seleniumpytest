from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME_INPUT = (By.XPATH, "//input[@placeholder='Username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Login']")
    DASHBOARD_TEXT = (By.XPATH, "//h1[contains(text(),'Dashboard')]")
