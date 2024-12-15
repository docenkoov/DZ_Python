from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        """
        Инициализация страницы корзины.
        :param driver: WebDriver для управления браузером.
        """
        self.driver = driver

    def add_to_cart(self, item_id: str) -> None:
        """
        Добавляет товар в корзину по его идентификатору.
        :param item_id: Идентификатор товара для добавления в корзину.
        """
        self.driver.find_element(By.ID, item_id).click()

    def go_to_cart(self) -> None:
        """
        Переходит на страницу корзины.
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
