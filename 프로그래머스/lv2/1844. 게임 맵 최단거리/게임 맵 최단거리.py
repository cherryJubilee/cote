from collections import deque

def solution(maps):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n = len(maps)
    m = len(maps[0])
    distance = [[0] * m for _ in range(n)]  # 각 위치까지의 최소 거리를 저장할 배열
    
    def bfs(x, y):
        Q = deque()
        Q.append((x, y))
        distance[x][y] = 1 # 시작 위치의 거리는 1
        
        while Q:  # 무한 루프 수정
            tmp = Q.popleft()
            for i in range(4):
                xx = tmp[0] + dx[i]
                yy = tmp[1] + dy[i]
                if 0 <= xx < n and 0 <= yy < m and maps[xx][yy] == 1:
                    if distance[xx][yy] == 0:
                        # 이전 위치의 거리 + 1을 저장
                        distance[xx][yy] = distance[tmp[0]][tmp[1]] + 1
                        # 큐에 새 위치를 추가
                        Q.append((xx, yy))
                    
        return distance[n-1][m-1] # 마지막 위치의 최소 거리를 반환

    answer = bfs(0, 0)
    if answer != 0:
        return answer
    else:
        return -1
