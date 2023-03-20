a, b, c, n = map(int, input().split())


def room():
    for z in range(n//a + 1):
        for y in range(n//b + 1):
            for x in range(n//c + 1):
                if (a * x) + (b * y) + (c * z) == n:
                    return 1

    return 0


print(room())