import pytest
from selenium import webdriver


@pytest.fixture
def setup():
    print("Настройка драйвера...")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()
    print("Драйвер завершил свою работу.")
