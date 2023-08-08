from collections import deque

# 방향을 나타내는 네 개의 좌표 (상, 우, 하, 좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())  # 보드의 크기를 입력 받음
board = [list(map(int, input().split())) for _ in range(n)]  # 2차원 보드 입력

cnt = 0  # 현재 그룹의 크기를 저장할 변수
Q = deque()  # BFS 탐색에 사용할 큐
res = []  # 각 그룹의 크기를 저장할 리스트

# 전체 보드를 탐색
for i in range(n):
    for j in range(n):
        # 만약 현재 위치가 1이면 (즉, 아직 방문하지 않은 그룹이면)
        if board[i][j] == 1:
            board[i][j] = 0  # 방문 표시
            Q.append((i, j))  # 현재 위치를 큐에 추가
            cnt = 1  # 현재 위치를 포함하여 그룹의 크기를 1로 시작

            # BFS 탐색 시작
            while Q:
                tmp = Q.popleft()  # 큐에서 위치를 하나 꺼냄
                for k in range(4):  # 꺼낸 위치의 네 방향을 탐색
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    # 범위 밖이거나 이미 방문한 위치 또는 장애물이 있는 경우 무시
                    if x < 0 or x >= n or y < 0 or y >= n or board[x][y] == 0:
                        continue
                    board[x][y] = 0  # 방문 표시
                    Q.append((x, y))  # 새로운 위치를 큐에 추가
                    cnt += 1  # 그룹의 크기 증가
            res.append(cnt)  # 그룹의 크기를 결과 리스트에 추가

# 결과 출력 부분
print(len(res))  # 그룹의 개수 출력
res.sort()  # 그룹의 크기를 오름차순으로 정렬
for x in res:
    print(x)  # 그룹의 크기를 순서대로 출력
