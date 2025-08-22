from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Brave()
browser.implicitly_wait(10)

browser.maximize_window()
browser.get("https://chercher.tech/practice/implicit-wait-example")

checkbox = browser.find_element(By.XPATH, "//input[@type='checkbox']")

assert checkbox.is_displayed()