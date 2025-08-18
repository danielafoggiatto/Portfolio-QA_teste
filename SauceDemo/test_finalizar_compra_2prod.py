from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import conftest

@pytest.mark.finalizar_compra
@pytest.mark.usefixtures("setup_teardown")
class TestCT04:
    def test_ct04_finalizar_compra_2prod(self):
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

        driver.find_element(By.XPATH, "//*[@id='checkout']").click()
        driver.find_element(By.ID, "first-name").send_keys("Daniela")
        driver.find_element(By.ID, "last-name").send_keys("Foggiatto")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()
        driver.find_element(By.ID, "finish").click()
