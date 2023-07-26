# 풀이 2 - library 이용 

import itertools as it
n, k = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())
cnt = 0

for x in it.combinations(a, k): # 리스트a에서 k개씩 조합
    if sum(x) % m == 0:
        cnt += 1
print(cnt)


'''
풀이 1
def dfs(level, start, sum):
    global cnt
    # 종착지점
    if level == k:
        if sum % m == 0:
            cnt += 1
    
    for i in range(start, n):
        dfs(level+1, i+1, sum + a[i]) # 이 부분 주의

n,k = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())
cnt = 0 
dfs(0,0,0) #(level, start, sum)

print(cnt)
'''
