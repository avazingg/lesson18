from time import sleep

import pytest

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

def test_login_and_add_to_cart():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://omayo.blogspot.com/")
        textbox1 = driver.find_element(By.ID, "textbox1")
        textbox1.clear()
        textbox1.send_keys("Selenium Test")
        assert textbox1.get_attribute("value") == "Selenium Test"


        drop1 = Select(driver.find_element(By.ID, "drop1"))
        drop1.select_by_visible_text("doc 3")

        assert drop1.first_selected_option.text == "doc 3"


    finally:
        # Закрытие браузера
        driver.quit()


