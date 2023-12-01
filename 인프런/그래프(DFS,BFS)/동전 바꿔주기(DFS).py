
def dfs(level, sum):
    global cnt
    if sum > T:
        return
    if level == K:
        if sum == T:
            cnt += 1 
    else:
        for i in range(count(level)+1): 
            dfs(level+1, sum+coin[level]*i)


T = int(input())
K = int(input())
coin = []
count = []
for _ in range(K):
    a, b = map(int, input().split())
    coin.append(a)
    count.append(b)
cnt = 0
dfs(0,0)
print(cnt)