from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class FormPage:
    """
    Класс для работы с формой на странице.
    Attributes:
        driver (WebDriver): Экземпляр драйвера Selenium.
    """

    def __init__(self, driver: webdriver):
        """
        Инициализация класса FormPage.

        Args:
            driver (webdriver): Экземпляр драйвера Selenium.
        """
        self.driver = driver

    def fill_first_name(self, name: str) -> None:
        """
        Заполнение поля имени.

        Args:
            name (str): Имя пользователя.
        """
        self.driver.find_element(
            By.CSS_SELECTOR,
            '.form-control[name="first-name"]').send_keys(name)

    def fill_last_name(self, name: str) -> None:
        """
        Заполнение поля фамилии.

        Args:
            name (str): Фамилия пользователя.
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="last-name"]').send_keys(name)

    def fill_address(self, address: str) -> None:
        """
        Заполнение поля адреса.

        Args:
            address (str): Адрес пользователя.
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '.form-control[name="address"]').send_keys(
                address)

    def fill_email(self, email: str) -> None:
        """
        Заполнение поля электронной почты.

        Args:
            email (str): Электронная почта пользователя.
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '.form-control[name="e-mail"]').send_keys(email)

    def fill_phone(self, phone: str) -> None:
        """
        Заполнение поля телефона.

        Args:
            phone (str): Телефон пользователя.
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '.form-control[name="phone"]').send_keys(phone)

    def fill_zip_code(self, zip_code: str) -> None:
        """
        Заполнение поля почтового индекса.

        Args:
            zip_code (str): Почтовый индекс.
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '.form-control[name="zip-code"]').send_keys(
                zip_code)

    def fill_city(self, city: str) -> None:
        """
        Заполнение поля города.

        Args:
            city (str): Город пользователя.
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '.form-control[name="city"]').send_keys(city)

    def fill_country(self, country: str) -> None:
        """
        Заполнение поля страны.
        Args:
            country (str): Страна пользователя.
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '.form-control[name="country"]').send_keys(
                country)

    def fill_job_position(self, position: str) -> None:
        """
        Заполнение поля должности.
        Args:
            position (str): Должность пользователя.
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '.form-control[name="job-position"]').send_keys(
                position)

    def fill_company(self, company: str) -> None:
        """
        Заполнение поля компании.

        Args:
            company (str): Название компании.
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '.form-control[name="company"]').send_keys(
                company)

    def submit(self) -> None:
        """
        Отправка формы.
        """
        button = self.driver.find_element(
            By.CSS_SELECTOR, '.btn.btn-outline-primary.mt-3')
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", button)
        ActionChains(self.driver).move_to_element(button).click().perform()
