from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.vars = {}
        self.session = SessionHelper(self)

    def open_home_page(self):
        # Step # | target | value | comment
        # open | /litecart/en/ |  |
        self.driver.get("http://localhost/litecart/en/")

    def open_category(self):
        # click | css=.category-1:nth-child(1) > a |  |
        self.driver.find_element(By.CSS_SELECTOR, ".category-1:nth-child(1) > a").click()

    def destroy(self):
        self.driver.quit()