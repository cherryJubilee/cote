def dfs(level, sum, time):
    global res
    if time > m:
        return
    if level == n:  # 부분집합 한개 완성 , 도착 지점인 경우
        if sum > res:
            res = sum
    else: # 종착지가 아닌경우 -> 뻗어나가자 (문제를 푼자 or 문제를 풀지 않는다)
        dfs(level+1, sum+pv[level], time+pm[level]) 
        dfs(level+1, sum, time)


pv = list()
pm = list()
n, m = map(int, input().split())
for _ in range(n):
    a, b= map(int, input().split())
    pv.append(a)  # 점수
    pm.append(b)  # 시간
res = -99900
dfs(0,0,0)  # 0번이 첫번째 문제