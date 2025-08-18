from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

def random_email():
    return "test_" + "".join(random.choices(string.ascii_lowercase + string.digits, k=5)) + "@mail.com"

def test_cadastro_login(driver):
    driver.get("https://automationexercise.com/login")
    

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "name"))
    )
    driver.find_element(By.NAME, "name").send_keys("Daniela")
    
    email = random_email()
    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(email)
    driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "id_gender2"))
    )
    driver.find_element(By.ID, "id_gender2").click()  # Mrs
    driver.find_element(By.ID, "password").send_keys("Senha123!")
    driver.find_element(By.ID, "days").send_keys("10")
    driver.find_element(By.ID, "months").send_keys("May")
    driver.find_element(By.ID, "years").send_keys("1990")
    driver.find_element(By.ID, "first_name").send_keys("Daniela")
    driver.find_element(By.ID, "last_name").send_keys("Foggiatto")
    driver.find_element(By.ID, "address1").send_keys("Rua Exemplo, 123")
    driver.find_element(By.ID, "country").send_keys("Canada")
    driver.find_element(By.ID, "state").send_keys("StateX")
    driver.find_element(By.ID, "city").send_keys("Florianópolis")
    driver.find_element(By.ID, "zipcode").send_keys("88000-000")
    driver.find_element(By.ID, "mobile_number").send_keys("48999999999")
    driver.find_element(By.XPATH, "//button[@data-qa='create-account']").click()

   
    account_msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//b[text()='Account Created!']"))
    ).text
    assert account_msg == "Account Created!"

    driver.find_element(By.XPATH, "//a[text()='Continue']").click()

    driver.find_element(By.XPATH, "//a[text()='Logout']").click()
    driver.get("https://automationexercise.com/login")  # abre direto login
    driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys(email)
    driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys("Senha123!")
    driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()

    welcome_msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//b[contains(text(),'Welcome')]"))
    ).text
    assert "Welcome" in welcome_msg

    driver.find_element(By.XPATH, "//a[text()='Logout']").click()
    driver.get("https://automationexercise.com/login")  # abre direto login
    driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("errado@mail.com")
    driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys("Senha123!")
    driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()

    error_msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[text()='Your email or password is incorrect!']"))
    ).text
    assert "incorrect" in error_msg

    driver.get("https://automationexercise.com/login")  # abre direto cadastro
    driver.find_element(By.NAME, "name").send_keys("Daniela")
    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(email)  # mesmo email usado
    driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

    exist_msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[text()='Email Address already exist!']"))
    ).text
    assert "already exist" in exist_msg
