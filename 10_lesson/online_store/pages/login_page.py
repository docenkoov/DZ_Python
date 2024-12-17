from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        """
        Инициализация страницы входа.
        :param driver: WebDriver для управления браузером.
        """
        self.driver = driver

    def enter_username(self, username: str) -> None:
        """
        Вводит имя пользователя в поле.
        :param username: Имя пользователя для входа.
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def enter_password(self, password: str) -> None:
        """
        Вводит пароль в поле.
        :param password: Пароль для входа.
        """
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self) -> None:
        """
        Нажимает кнопку входа.
        """
        self.driver.find_element(By.ID, "login-button").click()
