from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class FormPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_first_name(self, name):
        self.driver.find_element(By.CSS_SELECTOR,
                                 '.form-control[name="first-name"]').send_keys(
                                     name)

    def fill_last_name(self, name):
        self.driver.find_element(By.CSS_SELECTOR,
                                 '[name="last-name"]').send_keys(name)

    def fill_address(self, address):
        self.driver.find_element(By.CSS_SELECTOR,
                                 '.form-control[name="address"]').send_keys(
                                     address)

    def fill_email(self, email):
        self.driver.find_element(By.CSS_SELECTOR,
                                 '.form-control[name="e-mail"]').send_keys(
                                     email)

    def fill_phone(self, phone):
        self.driver.find_element(By.CSS_SELECTOR,
                                 '.form-control[name="phone"]').send_keys(
                                     phone)

    def fill_zip_code(self, zip_code):
        self.driver.find_element(By.CSS_SELECTOR,
                                 '.form-control[name="zip-code"]').send_keys(
                                     zip_code)

    def fill_city(self, city):
        self.driver.find_element(By.CSS_SELECTOR,
                                 '.form-control[name="city"]').send_keys(city)

    def fill_country(self, country):
        self.driver.find_element(By.CSS_SELECTOR,
                                 '.form-control[name="country"]').send_keys(
                                     country)

    def fill_job_position(self, position):
        self.driver.find_element(By.CSS_SELECTOR,
                                 '.form-control[name="job-position"]'
                                 ).send_keys(position)

    def fill_company(self, company):
        self.driver.find_element(By.CSS_SELECTOR,
                                 '.form-control[name="company"]').send_keys(
                                     company)

    def submit(self):
        button = self.driver.find_element(
            By.CSS_SELECTOR, '.btn.btn-outline-primary.mt-3')
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", button)
        ActionChains(self.driver).move_to_element(button).click().perform()
