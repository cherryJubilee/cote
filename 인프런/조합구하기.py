# 중요 - 응용 많이 됨

def dfs(level, start):
    global cnt
    if level == m:  # 종착점 일 때 출력
        for j in range(level):  # levle, m 상관없음
            print(res[j], end = ' ')
        cnt += 1
        print()

    else:
        for i in range(start, n+1):
            res[L] = i
            dfs(L+1, i + 1)  # s+1아니고 i+1이다 중요

n, m = map(int, input(.split()))
res = [0] * n+1  # 구슬의 총 개수인 n+1로 설정 
cnt = 0
dfs(0,1)  # dfs(level, start)