from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
import time

gecko_driver_path = r"D:\
    SKYPRO\TEST\Cours_4\geckodriver-v0.35.0-win64\geckodriver.exe"
service = Service(gecko_driver_path)

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/entry_ad")

try:
    wait = WebDriverWait(driver, 10)

    time.sleep(5)

    close_button = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "modal-footer"))
    )

    close_button.click()

    print("Кнопка закрытия нажата.")

    time.sleep(5)

finally:

    driver.quit()
