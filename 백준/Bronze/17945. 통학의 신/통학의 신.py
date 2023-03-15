import math
a, b = map(int, input().split())

x1 = -a - math.sqrt(a**2 - b)
x2 = -a + math.sqrt(a**2 - b)

if x1 == x2:
    print(int(x1))
else:
    print(int(x1), int(x2))