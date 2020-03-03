from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def logout(self):
        # click | linkText=Logout |  |
        wd = self.app
        wd.driver.find_element(By.LINK_TEXT, "Logout").click()

    def ensure_logout(self):
        wd = self.app
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app
        return len(wd.driver.find_elements(By.LINK_TEXT, "Logout")) > 0

    def is_logged_in_as(self, email):
        wd = self.app
        # в этом шаге должна быть проверка что залогинены под нужным пользователем - email
        return len(wd.driver.find_elements(By.LINK_TEXT, "Logout")) > 0

    def login(self, email, password):
        wd = self.app
        self.app.open_home_page()
        # click | name=email |  |
        wd.driver.find_element(By.NAME, "email").click()
        # type | name=email | san-100@bk.ru |
        wd.driver.find_element(By.NAME, "email").send_keys(email)
        # click | name=password |  |
        wd.driver.find_element(By.NAME, "password").click()
        # type | name=password | 1234 |
        wd.driver.find_element(By.NAME, "password").send_keys(password)
        # click | name=login |  |
        wd.driver.find_element(By.NAME, "login").click()

    def ensure_login(self, email, password):
        wd = self.app
        if self.is_logged_in():
            if self.is_logged_in_as(email):
                return
            else:
                self.logout()
        self.login(email, password)
