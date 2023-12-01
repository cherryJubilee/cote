def dfs(level, sum):
    global res
    if level == n+1: #level은 인덱스이자 날짜이다.
        if sum > res:
            res = sum
    else:
        # 상담을 한 경우
        if level + day[level] <= n+1:  # 이조건에 해당 되어야 가지를 뻗을 수 있다.
            dfs(level+day[level], sum+cost[level])
        # 상담을 하지 않은 경우
        dfs(level+1, sum)


        

n = int(input())
day = []
cost = []
for _ in range(n):
    a,b = map(int, input().split())
    day.append(a)
    cost.append(b)
res = -999999
# 인덱스를 날짜로 사용하기 위해 1씩 미뤄줌
day.insert(0,0)
cost.insert(0,0)
dfs(1,0)
print(res)