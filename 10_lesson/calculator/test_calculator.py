import pytest
import time
import allure
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


@allure.title("Тест калькулятора")
@allure.description("Проверка работы калькулятора на сложение")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator(driver):
    page = CalculatorPage(driver)

    with allure.step("Ввод значения 45"):
        page.enter_value("45")

    with allure.step("Нажатие кнопки 7"):
        page.press_button_7()

    with allure.step("Нажатие кнопки +"):
        page.press_plus()

    with allure.step("Нажатие кнопки 8"):
        page.press_button_8()

    with allure.step("Нажатие кнопки ="):
        page.press_equals()

    time.sleep(45)
    result = page.get_result()
    with allure.step("Проверка результата"):
        assert result == "15", f"Ожидалось 15, но получено {result}"
