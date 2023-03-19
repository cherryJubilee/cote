num = int(input())
count = 0

for a in range(num):
    for b in range(num):
        for c in range(num):
            if b >= a+2 and a >= 1 and c >= 1:
                if c % 2 == 0:
                    if a + b + c == num:
                        count += 1
print(count)