

# 입력받기
n, m = map(int, input().split()) # 정점의 수, 간선의 수
g = [[0] * (n+1) for _ in range(n+1)]
ch = [0] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1
cnt = 0
ch[1] =1 # 1번노드 방문함. 체크 하고 넘어감
dfs(1)

