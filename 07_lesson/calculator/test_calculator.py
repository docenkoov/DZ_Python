import pytest
from selenium import webdriver
from pages.calculator_page import CalculatorPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


def test_calculator(driver):
    page = CalculatorPage(driver)

    page.enter_value("45")

    page.press_button_7()
    page.press_plus()
    page.press_button_8()
    page.press_equals()

    result = page.get_result()
    assert result == "15", f"Ожидалось 15, но получено {result}"
