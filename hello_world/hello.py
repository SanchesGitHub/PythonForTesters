def hello(s):
    print('Hello, ' + s + '!')


hello("world")
hello("python")
hello("Alexander")

s1 = 'test'
s2 = '''test
test
test'''
s3 = s2[1:-1]
print(s1)
print(s2)
print(s3)
print(s1.startswith("te"))
print(s1.index("te"))
print(s1.find("te"))
print(s2.split("\n"))
print(" ".join(s1))
