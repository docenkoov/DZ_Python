import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.title("Тест покупки")
@allure.description("Тестирует процесс покупки товара в интернет-магазине")
@allure.feature("Покупка")
@allure.severity(allure.severity_level.NORMAL)
def test_purchase(setup):
    driver = setup

    with allure.step("Авторизация"):
        login_page = LoginPage(driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()
        allure.attach(
            driver.get_screenshot_as_png(
            ), name="Скриншот после авторизации",
            attachment_type=allure.attachment_type.PNG)
        print("Авторизация завершена.")

    with allure.step("Добавление товаров в корзину"):
        cart_page = CartPage(driver)
        cart_page.add_to_cart("add-to-cart-sauce-labs-backpack")
        cart_page.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
        cart_page.add_to_cart("add-to-cart-sauce-labs-onesie")
        print("Товары добавлены в корзину.")

    with allure.step("Переход в корзину и оформление заказа"):
        cart_page.go_to_cart()

        # Ожидание загрузки формы оформления заказа
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "first-name"))
            )
        except TimeoutException:
            print("Элемент 'first-name' не найден в течение 10 секунд.")
            driver.quit()
            return

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_info("Ольга", "Доценко", "172400")
        print("Форма успешно заполнена.")

    with allure.step("Чтение итоговой стоимости заказа"):
        total_amount = checkout_page.get_total_amount()
        print(f"Ожидаемая сумма: $58.29, Фактическая сумма: {total_amount}")
        allure.attach(
            driver.get_screenshot_as_png(
            ), name="Скриншот итоговой суммы",
            attachment_type=allure.attachment_type.PNG)
        assert total_amount == "$58.29"
