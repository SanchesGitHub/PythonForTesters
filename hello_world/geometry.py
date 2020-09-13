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

l8 = []
for i in range(-5, 6):
    l8.append(Point(i, i * i))

print(l8)

for el in l8:
    print(el)

l9 = []
for el in l8:
    l9.append(Point(el.x, -el.y))

print(l9)

l10 = [Point(i, i * i) for i in range(-5, 6)]
l11 = [Point(el.x, -el.y) for el in l8]

print(l10)
print(l11)

l12 = map(lambda i: Point(i, i * i), range(-5, 6))
print(l12)
l13 = map(lambda p: Point(p.x, -p.y), l12)
print(l13)
l14 = filter(lambda p: p.x >= 0, l12)
print(l14)
l15 = filter(lambda p: p.x % 2 == 0, l12)
print(l15)