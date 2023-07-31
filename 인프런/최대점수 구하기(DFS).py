'''
n: 문제 개수
m: 제한 시간
점수, 푸는데 걸리는 시간
'''

def dfs(level, sum, time): 
    global answer
    # 제한시간 m 을 넘어가면 안됨
    if time > m:
        return
    if level == n:
        if sum > answer:
            answer=sum
    else:
        # 문제를 푼 경우
        dfs(level+1, sum+score[level], time+time[level])
        # 문제를 풀지 않은 경우
        dfs(level+1, sum, time)


n, m = map(int, input().split())
score = []
time = []
for i in range(n):
    a, b = map(int, input().split())
    score.append(a)
    time.append(b)

answer = 0
dfs(0,0,0) #level, sum, time
print(answer)