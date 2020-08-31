from random import randrange

from model.duck import Duck


def test_open_duck(app):
    duck = Duck(name='Purple Duck', manufacturer='ACME Corp.', price='$0')

    app.group.open_category()
    ducks = app.group.get_duck_list()
    index = randrange(len(ducks))
    assert len(ducks) > 0
    assert ducks.__contains__(duck)
    app.group.open_duck()
    sort_ducks = sorted(ducks, key=Duck.id_or_name)


def test_open_duck_copy(app):
    duck = Duck(name='Purple Duck', manufacturer='ACME Corp.', price='$0')

    app.group.open_category()
    ducks = app.group.get_duck_list()
    assert len(ducks) > 0
    assert ducks.__contains__(duck)
    app.group.open_duck()
    sort_ducks = sorted(ducks, key=Duck.id_or_name)
