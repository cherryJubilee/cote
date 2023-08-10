from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 입력: 열 n, 행 m
n, m = map(int, input().split())  
# 보드의 상태 입력 (익었는지, 안익었는지)
board = [list(map(int, input().split())) for _ in range(m)]
# 각 위치에서 익는데 걸리는 날짜를 저장하는 배열
day = [[0] * n for _ in range(m)]  
Q = deque()

# 초기에 익은 토마토의 위치를 큐에 추가
for i in range(m):
    for j in range(n):
        if board[i][j] == 1:  
            Q.append((i, j))

# BFS 시작
while Q:
    tmp = Q.popleft()
    for k in range(4):
        x = tmp[0] + dx[k]
        y = tmp[1] + dy[k]
        # 경계 내에 있고, 아직 익지 않은 토마토인 경우
        if 0 <= x < m and 0 <= y < n and board[x][y] == 0:
            board[x][y] = 1  # 토마토를 익힘
            # 익는데 걸린 날짜 갱신 (부모 토마토의 날짜 + 1)
            day[x][y] = day[tmp[0]][tmp[1]] + 1  
            Q.append((x, y))  # 인접한 위치를 큐에 추가

# 모든 토마토가 익었는지 확인하는 플래그
flag = 1
for i in range(m):
    for j in range(n):
        # 안익은 토마토가 있다면
        if board[i][j] == 0:  
            flag = 0
            break

result = 0
# 모든 토마토가 익었다면
if flag == 1:
    # 가장 오래 걸린 날짜를 찾아서 결과에 저장
    for i in range(m):
        for j in range(n):
            if day[i][j] > result:
                result = day[i][j]
    print(result)
else:
    # 모든 토마토가 익지 않는다면 -1 출력
    print(-1)