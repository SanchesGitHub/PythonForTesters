# -*- coding: utf-8 -*-
class Duck:

    def __init__(self, name, manufacturer, price, id=None):
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.name, self.manufacturer, self.price)

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name and self.manufacturer == other.manufacturer and self.price == other.price

    def id_or_name(self):
        if self.id:
            return self.id
        else:
            return self.name
