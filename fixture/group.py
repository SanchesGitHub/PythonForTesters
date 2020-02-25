from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_category(self):
        # click | css=.category-1:nth-child(1) > a |  |
        wd = self.app
        wd.driver.find_element(By.CSS_SELECTOR, ".category-1:nth-child(1) > a").click()