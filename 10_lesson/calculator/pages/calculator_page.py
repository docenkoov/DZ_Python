from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    TimeoutException
)
import time
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализирует страницу калькулятора.

        :param driver: WebDriver - экземпляр драйвера Selenium.
        """
        self.driver = driver
        self.button_7 = (
            By.CSS_SELECTOR, "span.btn.btn-outline-primary:nth-child(1)")
        self.button_plus = (
            By.CSS_SELECTOR,
            "span.operator.btn.btn-outline-success:nth-child(4)")
        self.button_8 = (
            By.CSS_SELECTOR, "span.btn.btn-outline-primary:nth-child(2)")
        self.button_equals = (
            By.CSS_SELECTOR, "span.btn.btn-outline-warning:nth-child(15)")
        self.result_display = (By.CSS_SELECTOR, "div.screen")
        self.input_field = (By.CSS_SELECTOR, "input#result")

    def press_button_7(self):
        """Нажимает кнопку 7."""
        self._click_element(self.button_7)

    def press_plus(self):
        """Нажимает кнопку +."""
        self._click_element(self.button_plus)

    def press_button_8(self):
        """Нажимает кнопку 8."""
        self._click_element(self.button_8)

    def press_equals(self):
        """Нажимает кнопку = и ожидает появления результата."""
        self._click_element(self.button_equals)
        WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element(self.result_display, "15")
        )

    def get_result(self) -> str:
        """
        Получает результат вычисления.

        :return: str - текст результата.
        """
        result_element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.result_display)
        )
        return result_element.text.strip()

    def enter_value(self, value: str):
        """
        Вводит значение в поле ввода.

        :param value: str - значение для ввода.
        """
        try:
            input_element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.input_field)
            )
            input_element.clear()
            input_element.send_keys(value)
            time.sleep(1)
        except TimeoutException:
            print("Поле ввода не найдено на странице.")

    def _click_element(self, locator):
        """
        Нажимает на элемент, используя локатор.

        :param locator: tuple - локатор элемента.
        """
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script(
                "arguments[0].scrollIntoView();", element)
            time.sleep(1)
            element.click()
        except TimeoutException:
            print(f"Элемент {locator} не найден на странице.")
