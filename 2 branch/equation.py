import math
a = float(input())
b = float(input())
c = float(input())

D = b ** 2 - 4 * a * c
x1 = 0
x2 = 0
if D >= 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)

    print(x1)
    print(x2 if D > 0 else '')
