from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.implicitly_wait(10)

browser.maximize_window()
#browser.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")    

browser.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")

dropdown_products = Select(browser.find_element(By.XPATH, "//select[@id='first']"))
dropdown_products.select_by_visible_text("Google")

dropdown_animals = Select(browser.find_element(By.XPATH, "//select[@id='animals']"))
dropdown_animals.select_by_value("babycat")
dropdown_animals.select_by_index(4)

dropdown_food = Select(browser.find_element(By.XPATH, "//select[@id='second']"))
dropdown_food.select_by_visible_text
("Pizza")
dropdown_food.select_by_value("cheese")