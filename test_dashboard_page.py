from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,20)


    # Profile dropdown arrow
    profile_icon = (
        By.ID,
        "profile-click-icon"
    )


    # Logout option after dropdown opens
    logout_option = (
        By.XPATH,
        "//div[contains(text(),'Log out')]"
    )


    def logout(self):

        # Click profile arrow
        self.wait.until(
            EC.element_to_be_clickable(self.profile_icon)
        ).click()


        # Wait dropdown
        self.wait.until(
            EC.visibility_of_element_located(self.logout_option)
        )


        # Click logout
        self.wait.until(
            EC.element_to_be_clickable(self.logout_option)
        ).click()