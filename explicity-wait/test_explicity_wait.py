from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Brave()

browser.maximize_window()
browser.get("https://chercher.tech/practice/explicit-wait-example")
wait = webdriver.support.ui.WebDriverWait(browser, 15)

browser.find_element(By.ID, "alert").click()
wait.until(EC.alert_is_present() )

browser.find_element(By.ID, "populate-text").click()
wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*[@class='target-text']"), "Selenium Webdriver"))
target_text = browser.find_element(By.XPATH, "//*[@class='target-text']").text
assert target_text == "Selenium Webdriver"

browser.find_element(By.ID, "display-other-button").click()
wait.until(EC.element_to_be_clickable((By.ID, "hidden")))

browser.find_element(By.ID, "enable-button").click()
wait.until(EC.element_to_be_clickable((By.ID, "disable")))

checkbox = browser.find_element(By.ID, "ch").click()
wait.until(EC.element_to_be_selected(checkbox))

##forma mais resumida:
wait.until(EC.element_to_be_selected(browser.find_element(By.ID, "ch")))