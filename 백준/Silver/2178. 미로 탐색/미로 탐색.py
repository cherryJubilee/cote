
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y

            if 0 <= xx < n and 0 <= yy < m and board[xx][yy] == 1:
                board[xx][yy] = board[x][y] + 1 # 이동거리 업데이트
                queue.append((xx, yy))

    return board[n-1][m-1]
                

# 입력받기
n, m = map(int, input().split()) 
board = [list(map(int, input())) for _ in range(n)] 

#bfs 실행
print(bfs(0,0))