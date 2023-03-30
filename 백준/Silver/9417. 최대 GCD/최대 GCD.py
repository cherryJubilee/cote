def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i    # 역순으로 반복문이 실행되므로 가장 큰 i 반환


n = int(input())
for _ in range(n):
    num_list = list(map(int, input().split()))
    answer = [1]
    for i in range(0, len(num_list)-1):
        for j in range(i+1, len(num_list)):
            answer.append(gcd(num_list[i], num_list[j]))

    print(max(answer))