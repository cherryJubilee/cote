# 문제 개수
n = int(input())
result = list(map(int, input().split()))

count = 0
sum = 0
for i in range(len(result)):
    if result[i] == 1:
        count = count + 1
        sum = sum + count
    else:
        count = 0
print(sum)