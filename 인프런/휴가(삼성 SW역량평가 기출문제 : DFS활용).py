
def dfs(level, sum):
    global answer
    if level == n+1: # 절대 끝 지점을 넘어서는 안됨
        if sum > answer:
            answer = sum
    else:
        if level + day[level] <= n+1:
            # 상담 진행
            dfs(level + day[level], sum + benefit[level])
        # 다음 상담으로 건너 띄기
        dfs(level+1, sum)
    

n = int(input())
day = []
benefit = []

for i in range(n):
    a,b = map(int, input().split())
    day.append(a)
    benefit.append(b)

answer = 0
# 상담날짜(인덱스 = day)가 0이 아니라 1부터 시작하게 하기 위해서
day.insert(0,0)
benefit.insert(0,0)
dfs(1,0)

print(answer)