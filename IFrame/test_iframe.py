from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.implicitly_wait(10)

browser.maximize_window()

browser.get("https://chercher.tech/practice/practice/frames")

iframe1 = browser.find_element(By.XPATH, "//iframe[@id='frame1']")
browser.switch_to.frame(iframe1)
browser.find_element(By.XPATH, "//*[@id='topic']/following-sibling::input").send_keys("IFrame Test")

iframe3 = browser.find_element(By.ID, "frame3")
browser.switch_to.frame(iframe3)
checkbox = browser.find_element(By.XPATH, "//*[@type='checkbox']")
checkbox.click()

browser.switch_to.default_content()  

iframe2 = browser.find_element(By.XPATH, "//iframe[@id='frame2']")
browser.switch_to.frame(iframe2)
dropwdown_animals = Select(browser.find_element(By.XPATH, "//select[@id='animals']"))
dropwdown_animals.select_by_value("babycat")