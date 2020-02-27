from model.user import User


def test_login_and_logout(app):
    # Test name: Login and Logout
    user = User("san-100@bk.ru", "1234")
    app.session.login(email=user.email, password=user.password)
    app.group.open_category()
    app.session.logout()
