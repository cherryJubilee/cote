# [2960] 에라토스테네스의 체

N, K = map(int, input().split())
n_list = [False] * (N+1)
count = 0

for i in range(2, N+1):
    if n_list[i] == False:
        for j in range(i, N+1, i):
            if n_list[j] == False:
                n_list[j] = True
                count += 1
                if count == K:
                    print(j)
