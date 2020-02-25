from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def logout(self):
        # click | linkText=Logout |  |
        wd = self.app
        wd.driver.find_element(By.LINK_TEXT, "Logout").click()

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