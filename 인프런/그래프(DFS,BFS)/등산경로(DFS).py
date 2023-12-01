dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def dfs(x, y):
    global cnt
    if x == n and y == n:
        cnt += 1
    else:
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx <= n and 0 <= yy <= n and board[xx][yy] > board[x][y]:
                check[xx][yy] = 1
                dfs(xx, yy)
                check[xx][yy] = 0




n = int(input())
board = [[0]*n for _ in range(n)]
check = [[0]*n for _ in range(n)]
max = 99999
main = -9999

# 실제 입력 받는 부분
for i in range(n):
    tmp = list(map(int, input().split()))  # 한 행 읽어오기.
    for j in range(n):
        # 최솟값 찾기
        if tmp[j] < min:
            min = tmp[j]
            start_x = i
            start_y = j
        # 최댓값 찾기
        if tmp[j] > max:
            max = tmp[j]
            end_x = i
            end_y = j
        board[i][j] = tmp[j]
check[start_x][start_y] = 1
cnt = 0
dfs(start_x, start_y)
print(cnt)
# 가장 낮은 지점 -> 가장 큰 지점으로 이동, 입력 값에 따라 바뀔 수 있다.
# 현재 지점보다 높은 곳으로만 이동해야된다.

