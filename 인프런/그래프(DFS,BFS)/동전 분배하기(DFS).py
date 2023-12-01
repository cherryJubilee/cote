
def dfs(level):
    global res
    if level == n:
        # 답 구하기
        cha = max(money) - min(money)
        if cha < res:
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:
                res = cha

    else:
        for i in range(3):  # 0, 1, 2번째 사람
            money[i] += coin[level]
            dfs(level+1)
            money[i] -= coin[level]




n = int(input())
coin = []
money = [0] * 3
res = 99000
for _ in range(n):
    a = int(input())
    coin.append(a)
dfs(0)
