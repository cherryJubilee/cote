from collections import deque

# 대각선까지 포함한 8방향을 정의
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
Q = deque()

for i in range(n):
    for j in range(n):
        # 섬의 한 부분 발견
        if board[i][j] == 1: 
            board[i][j] = 0  # 해당 부분을 0으로 설정
            Q.append((i, j))  # 시작점을 큐에 추가
            # 큐가 빌 때까지 BFS 실행
            while Q:
                tmp = Q.popleft()
                for k in range(8):  # 8 방향으로 탐색
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    # 만약 탐색된 부분이 board의 범위 내에 있고, 섬의 부분이라면
                    if 0 <= x < n and 0 <= y < n and board[x][y] == 1:
                        board[x][y] = 0  # 방문한 부분은 0으로 설정
                        # ⭐️탐색한 부분의 주변을 다음 BFS 단계에서 탐색하기 위해 큐에 추가
                        Q.append((x, y))  
            
            # 연결된 섬의 모든 부분을 탐색했으므로 섬의 개수를 증가
            cnt += 1

print(cnt)
