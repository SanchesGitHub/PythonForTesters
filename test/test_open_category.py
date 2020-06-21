def test_open_category(app):
    app.group.open_category()
    ducks = app.group.get_duck_list()
    assert len(ducks) > 0
