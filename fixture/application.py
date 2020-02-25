from selenium import webdriver
from selenium.webdriver.common.by import By


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def open_home_page(self):
        # Step # | target | value | comment
        # open | /litecart/en/ |  |
        self.driver.get("http://localhost/litecart/en/")

    def open_category(self):
        # click | css=.category-1:nth-child(1) > a |  |
        self.driver.find_element(By.CSS_SELECTOR, ".category-1:nth-child(1) > a").click()

    def logout(self):
        # click | linkText=Logout |  |
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

    def login(self, email, password):
        self.open_home_page()
        # click | name=email |  |
        self.driver.find_element(By.NAME, "email").click()
        # type | name=email | san-100@bk.ru |
        self.driver.find_element(By.NAME, "email").send_keys(email)
        # click | name=password |  |
        self.driver.find_element(By.NAME, "password").click()
        # type | name=password | 1234 |
        self.driver.find_element(By.NAME, "password").send_keys(password)
        # click | name=login |  |
        self.driver.find_element(By.NAME, "login").click()

    def destroy(self):
        self.driver.quit()