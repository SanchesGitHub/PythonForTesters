# Selenium
import pytest
from application import Application
from user import User


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_login_and_logout(app):
    # Test name: Login and Logout
    user = User("san-100@bk.ru", "1234")
    app.login(email=user.email, password=user.password)
    app.open_category()
    app.logout()
