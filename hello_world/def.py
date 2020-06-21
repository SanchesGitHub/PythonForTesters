def percents(x, y):
    """Function"""
    one_percent = x / 100
    result = y / one_percent
    return result


def print_percents(x, y):
    """Print"""
    print(str(y) + ' is ' + str(percents(x, y)) + '% of ' + str(x))


percents(200, 50)


print_percents(200, 50)
