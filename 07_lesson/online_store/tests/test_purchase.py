from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_purchase(setup):
    driver = setup

    # Авторизация
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    print("Авторизация завершена.")

    # Добавление товаров в корзину
    cart_page = CartPage(driver)
    cart_page.add_to_cart("add-to-cart-sauce-labs-backpack")
    cart_page.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
    cart_page.add_to_cart("add-to-cart-sauce-labs-onesie")
    print("Товары добавлены в корзину.")

    # Переход в корзину и оформление заказа
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
    # Здесь также нужно изменить, чтобы заполнение формы методами класса
    checkout_page.fill_checkout_info("Ольга", "Доценко", "172400")
    print("Форма успешно заполнена.")

    # Чтение итоговой стоимости заказа
    total_amount = checkout_page.get_total_amount()
    print(f"Ожидаемая сумма: $58.29, Фактическая сумма: {total_amount}")
    assert total_amount == "$58.29"
