dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    global cnt
    if x == 6 and y == 6:
        cnt += 1
    else:
        for i in range(4):
            # 새로 갈 지점 xx, yy
            xx = x + dx[i] 
            yy = y + dy[i] 
            if 0<=xx<=6 and 0<=yy<=6 and board[xx][yy] == 0:
                board[xx][yy] == 1
                dfs(xx, yy)
                # 빽 해야되니까 
                board[xx][yy] == 0

board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
board[0][0] = 1 # 출발점 
dfs(0, 0)  # 출발 지점
print(cnt)
