
'''
파이썬 2차원 리스트에 접근하는 방법
list[row][column]
'''
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
a = [list(map(int, input().split())) for _ in range(7)]
dis = [[0] * 7 for _ in range(7)]  # 도착지까지의 이동횟수를 알아보기 위함 -> dis[6][6] 

# BFS를 위한 큐 생성 및 시작점 (0,0)을 큐에 삽입
Q = deque()
Q.append((0,0)) # 출발지점, 튜플 형식으로 적기!

# 시작점을 방문했다는 표시를 위해 1(벽)로 변경
a[0][0] = 1 

while Q: # 큐에 값이 있을 동안 반복
    tmp = Q.popleft()  # (0,0)
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        # 경계선 범위 내에 있고, 아직 방문하지 않은 곳이면
        if 0 <= x <= 6 and 0 <= y <= 6 and a[x][y] == 0:
            a[x][y] = 1   # 방문 표시
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1   # 이동 횟수 갱신
            Q.append((x, y))  # 큐에 새로운 위치 추가

if dis[6][6] == 0:
    print(-1)
else:
    print(dis[6][6])