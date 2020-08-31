from geom2d.point import *

a = Point(0, 0)
b = Point(3, 4)
print(a.distance(b))
print(a == Point(0, 0))
print(a == b)
print(b)

l1 = [1, 5, 3, 7, 2, 8]
print(l1)
l2 = sorted(l1)
print(l2)

l3 = [b, a, Point(1, 5)]
print(l3)
l4 = sorted(l3)
print(l4)

m1 = [Point]

l5 = sorted(l3, key=lambda p: p.x)
print(l5)
l6 = sorted(l3, key=lambda p: p.y)
print(l6)
l7 = sorted(l3, key=lambda p: p.distance(Point(0, 0)))
print(l7)

# def cmp(a, b):
#     return (a > b) - (a < b)
# l8 = sorted(l3, cmp=lambda p1, p2: cmp(p1.y, p2.y))
# print(l8)
