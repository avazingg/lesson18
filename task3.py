import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

def test_login_and_add_to_cart():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://demoqa.com/webtables")
        addElement = driver.find_element(By.ID, "addNewRecordButton")
        addElement.click()
        driver.find_element(By.ID, "firstName").send_keys("John")
        driver.find_element(By.ID, "lastName").send_keys("Doe")
        driver.find_element(By.ID, "userEmail").send_keys("john.doe@example.com")
        driver.find_element(By.ID, "age").send_keys("30")
        driver.find_element(By.ID, "salary").send_keys("50000")
        driver.find_element(By.ID, "department").send_keys("IT")
        driver.find_element(By.ID, "submit").click()


        assert driver.find_element(By.XPATH, "//div[text()='John']") is not None, "John not found in the table"
        driver.find_element(By.ID, "edit-record-4").click()
        age = driver.find_element(By.ID, "age")
        salary = driver.find_element(By.ID, "salary")

        assert age.get_attribute("value") == "30"
        assert salary.get_attribute("value") == "50000"

        age.clear()
        age.send_keys("35")
        salary.clear()
        salary.send_keys("55000")

        assert age.get_attribute("value") == "35"
        assert salary.get_attribute("value") == "55000"

        driver.find_element(By.ID, "submit").click()

        driver.find_element(By.ID,"delete-record-4").click()

        elements = driver.find_elements(By.XPATH, "//div[text()='John']")
        assert len(elements) == 0, "John is still present in the table"

    finally:
        # Закрытие браузера
        driver.quit()


