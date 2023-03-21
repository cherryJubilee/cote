N = int(input())
answer = []

for _ in range(N):
    num = int(input())
    verify = False
    for i in range(2, 1000001):
        if num % i == 0:
            answer.append("NO")
            verify = True
            break
    if verify is False:
        answer.append("YES")


for i in answer:
    print(i)