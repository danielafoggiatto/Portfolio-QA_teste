import pytest
from selenium import webdriver

driver: webdriver.Remote

@pytest.fixture
def setup_teardown():
    global driver
    driver = webdriver.Edge()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    yield
    driver.quit()