'''
무방향 그래프인 경우
for i in range(m):
    a, b = map(imt, imput(split()))
    g[a][b] = 1
    g[b][a] = 1
'''

# 입력 받기
g = [[0] * (n+1) for _ in range(n+1)] # 2차 배열
for i in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = c # 가중치가 있는 방향 그래프이므로 g[b][a]는 하면 안됨

# 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end = ' ')
    print()