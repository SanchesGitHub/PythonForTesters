import pytest

from fixture.application import Application
from model.user import User

fixture = None


@pytest.fixture
def app(request):
    global fixture
    user = create_user()
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(email=user.email, password=user.password)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)


def create_user(email="san-100@bk.ru", password="1234"):
    user = User(email, password)
    return user