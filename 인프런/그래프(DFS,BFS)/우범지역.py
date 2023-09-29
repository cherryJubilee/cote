# 우범지역(DFS)


def dfs(c, K, visited, graph, crime):
    visited[c] = True
    count = crime[c]
    for i in range(len(graph)):
        if graph[c][i] == 1 and visited[i] = 0 and K > 0:
            count += dfs(i, K-1, visited, graph, crime)
    visited[c] = False
    return count

def solve():
    T = int(input())
    for t in range(1, T+1):
        N, K = map(int, input().split()) 
        graph = [[0] * (N+1) for _ in range(N+1)]
        for _ in range(N-1): 
            a, b = map(int, input().split()) 
            graph[a][b] = 1
            graph[b][a] = 1

        crime = [0] + list(map(int, input().split()))
        visited = [False] * (N+1)
        total = 0  

        for i in range(1, N+1):
            total += dfs(i, K, visited, graph, crime)  

        print(f'#{t} {total}') 
solve()
