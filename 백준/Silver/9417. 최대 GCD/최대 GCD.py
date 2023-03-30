import math

n = int(input())
for _ in range(n):
    num_list = list(map(int, input().split()))
    answer = [1]
    for i in range(0, len(num_list)-1):
        for j in range(i+1, len(num_list)):
            answer.append(math.gcd(num_list[i], num_list[j]))
    print(max(answer))