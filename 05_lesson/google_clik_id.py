from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/dynamicid")

blue_button = driver.find_element(
    By.XPATH, "//button[contains(@class, 'btn btn-primary')]")
blue_button.click()

time.sleep(5)
driver.quit()
