from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import conftest
from Pages.login_page import LoginPage

@pytest.mark.login
@pytest.mark.usefixtures("setup_teardown")
class TestCT02:
    def test_ct02_login_valido(self):
        driver = conftest.driver
        login_page = LoginPage()
        login_page.fazer_login("standard_user", "secret_sauce")

        assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()
