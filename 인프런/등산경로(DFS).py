dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    global cnt
    # 도착지점에 도착하면 카운트 올려주기
    if x == end_x and y == end_y:
        cnt += 1

    else:
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= x < n and 0 <= y <n and check[xx][yy] == 0 and board[xx][yy] > board[x][y]:
                check[xx][yy] = 1
                dfs(xx, yy)
                check[xx][yy] = 0


n = int(input())
board = [[0] * n for _ in range(n)]
check = [[0] * n for _ in range(n)]
max = 21470000
min = -21470000
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] < min:
            min = tmp[j]
            start_x = i
            start_y = j
        if tmp[j] > max:
            max = tmp[j]
            end_x = i
            end_y = j
        board[i][j] = tmp[j]
check[start_x][start_y] = 1
cnt = 0
dfs(start_x, start_y)
print(cnt)