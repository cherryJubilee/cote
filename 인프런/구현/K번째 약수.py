n, m = map(int, input().split())

answer = []
for i in range(1, n+1):
    if n % i == 0:
        answer.append(i)

if len(answer) < m:  # 약수의 개수가 m보다 작은 경우
    print(-1)
else:
    print(answer[m-1])
