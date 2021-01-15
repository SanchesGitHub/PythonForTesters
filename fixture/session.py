from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def logout(self):
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
        # в этом шаге должна быть проверка что залогинены под
        # нужным пользователем - email
        return len(wd.driver.find_elements(By.LINK_TEXT, "Logout")) > 0

    def login(self, email, password):
        wd = self.app
        self.app.open_home_page()
        wd.driver.find_element(By.NAME, "email").click()
        wd.driver.find_element(By.NAME, "email").send_keys(email)
        wd.driver.find_element(By.NAME, "password").click()
        wd.driver.find_element(By.NAME, "password").send_keys(password)
        wd.driver.find_element(By.NAME, "login").click()

    def ensure_login(self, email, password):
        wd = self.app
        if self.is_logged_in():
            if self.is_logged_in_as(email):
                return
            else:
                self.logout()
        self.login(email, password)
