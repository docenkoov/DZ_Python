from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа.
        :param driver: WebDriver для управления браузером.
        """
        self.driver = driver

    def fill_checkout_info(
            self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет форму оформления заказа.
        :param first_name: Имя покупателя.
        :param last_name: Фамилия покупателя.
        :param postal_code: Почтовый индекс.
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total_amount(self) -> str:
        """
        Получает итоговую сумму заказа.
        :return: Итоговая сумма в виде строки.
        """
        total_element = self.driver.find_element(
            By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text
        return total_text.split()[-1]
