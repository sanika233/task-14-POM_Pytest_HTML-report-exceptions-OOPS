from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        # Update these locators after inspecting Zen Portal
        self.username = (By.XPATH, "//input[contains(@placeholder,'mail')]")
        self.password = (By.XPATH, "//input[@type='password']")
        self.login_btn = (By.XPATH, "//button[@type='submit']")

    def enter_username(self, uname):
        try:
            username_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.username)
            )
            username_field.clear()
            username_field.send_keys(uname)

        except TimeoutException:
            print("Username field not found")

    def enter_password(self, pwd):
        try:
            password_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.password)
            )
            password_field.clear()
            password_field.send_keys(pwd)

        except TimeoutException:
            print("Password field not found")

    def click_login(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.login_btn)
            ).click()

        except TimeoutException:
            print("Login button not found")

    def login(self, uname, pwd):
        self.enter_username(uname)
        self.enter_password(pwd)
        self.click_login()