"""
단지번호 붙이기 - 백준 실버 1
"""
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 단지 속 집의 수 count
def dfs(x, y):
    global cnt 
    cnt += 1 # 집의 수 세는거니까 일단 해당 집 +1 하고 시작
    board[x][y] = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[j]
        if 0<=xx<n and 0<=yy<n and board[xx][yy] == 1:
            dfs(xx, yy)

n = int(input())
board = [list(map(int, input())) for _ in range(n)]
res = []
# 단지 수 count
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            # 새로운 단지를 발견할 때마다 cnt는 0으로 초기화
            cnt = 0
            dfs(i, j)
            # dfs돌고와서 한 단지에 속하는 집의 수 append
            res.append(cnt)
    
print(len(res))
res.sort()
for x in res:
    print(x)