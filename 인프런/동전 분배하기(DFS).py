def dfs(level):
    global res
    # 끝점
    # 총액이 가장 큰 사람과 가장 작은 사람의 차가 최소가 되도록 하기
    if level == n:
        max_min = max(money) - min(money)
        if max_min < res:
            # 단 세 사람의 총액은 서로 달라야 합니다. 
            tmp = set()  # set은 중복 안됨
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:
                # 차가 최소이고, 세 사람의 총액이 서로 다를때만 업데이트
                res = max_min 

    else:
        # 가지 표현
        for i in range(3):  #나눠 줘야 할 사람이 3명이다
            money[i] += coins[level]
            dfs(level+1)
            # 취소,back 하는 상황
            money[i] -= coins[level]





n = int(input()) # 동전 개수
coins = []
money = [0] * 3 # 각 사람의 금액 (3명 이니까)
res = 0  # 차의 최솟값
for i in range(n):
    coins.append(int(input))

dfs(0)
print(res)