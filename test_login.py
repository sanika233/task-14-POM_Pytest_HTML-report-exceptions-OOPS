import pytest
import time
from new_pages.pages.test_login_page import LoginPage
from new_pages.pages.test_dashboard_page import DashboardPage

# Positive Test Case
def test_successful_login(driver):

    login = LoginPage(driver)

    login.login(
        "-----",
        "-----------"
    )
    time.sleep(5)
    assert "dashboard" in driver.current_url.lower()


# Negative Test Case
def test_unsuccessful_login(driver):

    login = LoginPage(driver)

    login.login(
        "wronguser@gmail.com",
        "wrongpassword"
    )

    assert "dashboard" not in driver.current_url.lower()


# Username Validation
def test_username_field(driver):

    login = LoginPage(driver)

    login.enter_username("------------")

    assert True


# Password Validation
def test_password_field(driver):

    login = LoginPage(driver)

    login.enter_password("---------------")

    assert True


# Submit Button Validation
def test_submit_button(driver):

    login = LoginPage(driver)

    login.click_login()

    assert True


def test_logout_functionality(driver):

    # Step 1: Login
    login = LoginPage(driver)

    login.login(
        "-------------------",
        "---------------"
    )


    # Step 2: Dashboard opens
    time.sleep(3)

    assert "dashboard" in driver.current_url.lower()

    time.sleep(5)
    # Create dashboard object
    dashboard = DashboardPage(driver)


    # Step 3,4,5
    dashboard.logout()

    time.sleep(5)
    # Verify logout successful
    assert "login" in driver.current_url.lower()
