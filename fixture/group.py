from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from model.duck import Duck


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_category(self):
        wd = self.app
        wd.driver.find_element(By.CSS_SELECTOR, ".category-1:nth-child(1) > a").click()

    def open_duck(self):
        wd = self.app
        wd.driver.find_element(By.XPATH, ".//div[@class='name' and text()='Purple Duck']").click()

    def search_duck(self, text=None):
        wd = self.app
        if text is not None:
            wd.driver.find_element(By.XPATH, ".//input[@placeholder='Search' and @name='query']").click()
            wd.driver.find_element(By.XPATH, ".//input[@placeholder='Search' and @name='query']").send_keys(text,Keys.ENTER)

    def get_duck_list(self):
        wd = self.app
        ducks = []
        for element in wd.driver.find_elements(By.XPATH, ".//ul/li/a[div[@class='name']]"):
            name = element.find_element_by_class_name("name").text
            manufacturer = element.find_element_by_class_name("manufacturer").text
            price = element.find_element(By.XPATH, ".//div/*[contains(@class, 'price')]").text
            ducks.append(Duck(name=name, manufacturer=manufacturer, price=price))
        return ducks

