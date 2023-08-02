def dfs(level, sum):
    global cnt
    # 말단 노드이고, 여기까지의 합이 20(t) 라면 카운트 해줄것 
    if level == k: 
        if sum == t:
            cnt += 1

    # 가지 그려주기
    else:
        for i in range(amount[level]+1):
            dfs(level+1, sum + coins[level])


t = int(input()) # 금액
k  = int(input() ) # 동전 가지수

coins = [] # 동전의 금액
amount = [] # 동전의 개수
for i in range(k):
    p, n = map(int, input().split())
    coins.append(p)
    amount.append(p)

cnt = 0
dfs(0, 0) # dfs(level, sum)

# level은 동전의 금액을 말한다.
# sum은 선택된 동전의 합
print(cnt)