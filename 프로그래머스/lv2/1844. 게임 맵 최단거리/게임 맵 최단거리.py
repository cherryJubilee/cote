from collections import deque

def solution(maps):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n = len(maps)
    m = len(maps[0])
    distance = [[-1] * m for _ in range(n)] # distance 초기화 수정

    def bfs(x, y):
        Q = deque()
        Q.append((x, y))
        distance[x][y] = 1 # 시작 위치의 거리를 1로 초기화

        while Q: # 무한루프 수정
            x, y = Q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                    if distance[nx][ny] == -1: # 중복 방문 방지
                        distance[nx][ny] = distance[x][y] + 1
                        Q.append((nx, ny))
        return distance[n-1][m-1] # 마지막 위치의 최소 거리를 반환

    answer = bfs(0, 0)
    return answer if answer != -1 else -1 # 최종 결과 반환
