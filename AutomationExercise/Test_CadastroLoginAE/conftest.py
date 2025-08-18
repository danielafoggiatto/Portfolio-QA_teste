import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time

@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--start-maximized")

    driver = webdriver.Edge(options=opts)
    driver.get("https://automationexercise.com/login") 

    yield driver

    time.sleep(5)
    driver.quit()
