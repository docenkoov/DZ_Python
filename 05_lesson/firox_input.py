from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/inputs")

    input_field = driver.find_element(By.TAG_NAME, "input")

    input_field.send_keys("1000")

    time.sleep(5)

    input_field.clear()
    time.sleep(3)

    input_field.send_keys("999")

    time.sleep(3)

finally:
    driver.quit()
