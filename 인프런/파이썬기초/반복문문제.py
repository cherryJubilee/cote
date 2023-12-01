# 1. 1부터 N 까지 홀수 출력
N = 10
for i in range(1, N+1):
    if i % 2 == 1:
        print(i)

# 2. 1부터 N 까지 합 출력
sum = 0
for i in range(1, N+1):
    sum += i
print(sum)

    
# 3. N의 약수 출력
N = 20
for i in range(1, N+1):
    if N % i == 0:
        print(i, end=",") # 1,2,4,5,10,20