def test_open_duck(app):
    app.group.open_category()
    ducks = app.group.get_duck_list()
    assert len(ducks) > 0
    app.group.open_duck()