# -*- coding: utf-8 -*-


def test_phone_number(app):
    phone = app.group.get_phone_number()
    # далее сравнение с эталонными данными
