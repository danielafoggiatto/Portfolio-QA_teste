from selenium.webdriver.common.by import By
from selenium import webdriver

def test_login_sucesso():
    browser = webdriver.Edge()
    browser.maximize_window()
    browser.get("https://www.saucedemo.com/")

    username = browser.find_element(By.ID, "user-name")
    password = browser.find_element(By.ID, "password")
    btn_login = browser.find_element(By.ID, "login-button")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    btn_login.click()

    products_title = browser.find_element(By.XPATH, "//span[@class='title']")
    assert products_title.text == "Products"

    img_backpack = browser.find_element(By.XPATH, "//img[@alt='Sauce Labs Backpack']")
    print(img_backpack.get_attribute("alt"))

    browser.quit()
