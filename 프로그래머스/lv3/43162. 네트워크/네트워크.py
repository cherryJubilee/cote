from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0] * n  # 방문 여부를 기록하는 리스트
    
    def bfs(node):
        q = deque([node])
        while q:
            v = q.popleft()
            visited[v] = 1  # 노드 방문 처리
            for i in range(n):
                if computers[v][i] == 1 and not visited[i]:  # 연결되어 있고 아직 방문하지 않았다면
                    q.append(i)
                    computers[v][i] = computers[i][v] = 0  # 해당 연결 처리(양방향이므로 두 군데 모두 0으로 처리)

    for i in range(n):
        if not visited[i]:  # 노드를 방문하지 않았다면
            bfs(i)  # bfs로 연결된 모든 노드들 방문 처리
            answer += 1  # 네트워크 개수 증가

    return answer
        
    