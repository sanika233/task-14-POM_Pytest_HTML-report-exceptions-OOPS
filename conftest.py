from selenium import webdriver
import pytest

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://v2.zenclass.in/login")

    print("Current URL:", driver.current_url)
    print("Title:", driver.title)

    yield driver

    driver.quit()