import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.page_object import FormPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестирование отправки формы")
@allure.description("Проверка корректности заполнения формы")
@allure.feature("Форма")
@allure.severity(allure.severity_level.NORMAL)
def test_form_submission(driver):
    with allure.step("Открытие страницы"):
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    form_page = FormPage(driver)

    with allure.step("Заполнение формы"):
        form_page.fill_first_name('Иван')
        form_page.fill_last_name('Петров')
        form_page.fill_address('Ленина, 55-3')
        form_page.fill_email('test@skypro.com')
        form_page.fill_phone('+7985899998787')
        form_page.fill_zip_code('')
        form_page.fill_city('Москва')
        form_page.fill_country('Россия')
        form_page.fill_job_position('QA')
        form_page.fill_company('SkyPro')

    with allure.step("Отправка формы"):
        form_page.submit()

    with allure.step("Проверка результатов"):
        WebDriverWait(driver, 40).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#zip-code'))
        )

        assert 'alert-danger' in driver.find_element(
            By.CSS_SELECTOR, '#zip-code').get_attribute("class")
        assert 'success' in driver.find_element(
            By.CSS_SELECTOR, '#first-name').get_attribute("class")
        assert 'success' in driver.find_element(
            By.CSS_SELECTOR, '#last-name').get_attribute("class")
        assert 'success' in driver.find_element(
            By.CSS_SELECTOR, '#address').get_attribute("class")
        assert 'success' in driver.find_element(
            By.CSS_SELECTOR, '#e-mail').get_attribute("class")
        assert 'success' in driver.find_element(
            By.CSS_SELECTOR, '#phone').get_attribute("class")
        assert 'success' in driver.find_element(
            By.CSS_SELECTOR, '#city').get_attribute("class")
