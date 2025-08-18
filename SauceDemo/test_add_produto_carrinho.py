from selenium.webdriver.common.by import By
import pytest
import conftest

@pytest.mark.carrinho
@pytest.mark.usefixtures("setup_teardown")
class TestCT01:
    def test_ct01_add_produto_carrinho(self):
        driver = conftest.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys('secret_sauce')
        driver.find_element(By.ID, "login-button").click()

        driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']").click()

        driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()

        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()

        driver.find_element(By.ID, "continue-shopping").click()
        driver.find_element(By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']").click()
        driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
