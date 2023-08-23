# 바텀 엎 방식
'''
n = int(input())
dy = [0] * (n+1)
dy[1] = 1
dy[2] = 2

for i in range(3, n+1):
    dy[i] = dy[i-1] + dy[i-2] 

print(dy[n])
'''
# 탑 다운 방식

def dfs(len):
    if dy[len] > 0:
        return dy[len]
    if len == 1 or len == 2:
        return len
    else:
        dy[len] = dfs[len-1] + dfs[len-2]
        return dy[len]


n = int(input())
dy = [0] * (n+1)
print