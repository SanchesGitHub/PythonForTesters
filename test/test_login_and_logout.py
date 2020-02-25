# Selenium
import pytest
from fixture.application import Application
from model.user import User


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
