from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import conftest

@pytest.mark.login
@pytest.mark.usefixtures("setup_teardown")
class TestCT03:
    def test_ct03_login_senha_invalida(self):
        driver = conftest.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("wrong_password")
        driver.find_element(By.ID, "login-button").click()

