import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def setup():
    print("Настройка драйвера...")
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()
    print("Драйвер завершил свою работу.")


def test_purchase(setup):
    driver = setup

    print("Авторизация на сайте...")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    print("Авторизация завершена.")

    print("Добавление товаров в корзину...")
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    print("Товары добавлены в корзину.")

    print("Переход в корзину...")
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    print("Переход к оформлению заказа...")
    driver.find_element(By.ID, "checkout").click()

    print("Заполнение формы для оформления заказа...")
    driver.find_element(By.ID, "first-name").send_keys("Ольга")
    driver.find_element(By.ID, "last-name").send_keys("Доценко")
    driver.find_element(By.ID, "postal-code").send_keys("172400")
    driver.find_element(By.ID, "continue").click()
    print("Форма успешно заполнена.")

    print("Чтение итоговой стоимости заказа...")
    total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total_text = total_element.text
    total_amount = total_text.split()[-1]

    print(f"Ожидаемая сумма: $58.29, Фактическая сумма: {total_amount}")
    assert total_amount == "$58.29"


if __name__ == "__main__":
    pytest.main()
