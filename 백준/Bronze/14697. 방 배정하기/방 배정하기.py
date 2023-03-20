a, b, c, n = map(int, input().split())


def room():
    for x in range(1, 51):
        for y in range(x, 51):
            for z in range(y, 51):
                if (a * x) + (b * y) + (c * z) == n:
                    return 1

    return 0


print(room())