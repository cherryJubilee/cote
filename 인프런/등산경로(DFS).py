dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    global cnt
    # 도착지점에 도착하면 카운트 올려주기
    if x == end_x and y == end_y:
        cnt += 1

    else:
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < n and 0 <= yy <n and check[xx][yy] == 0 and board[xx][yy] > board[x][y]:
                check[xx][yy] = 1  # 해당 위치 방문 표시
                dfs(xx, yy)  # 새로운 위치에서 DFS 시작
                check[xx][yy] = 0  # DFS 후에는 방문 표시 제거 (다른 경로를 통해 재방문 가능하도록)


n = int(input())
board = [[0] * n for _ in range(n)]  # n x n 등산 지도 생성하고 아래 for문을 통해 등산지도 업뎃
check = [[0] * n for _ in range(n)]  # n x n 체크 리스트 생성 (방문 여부 표시)
max = -21470000
min = 21470000

# 등산 지도 정보 입력 받기
for i in range(n):
    tmp = list(map(int, input().split()))  # 한 줄의 등산 지도 정보 입력 받기
    for j in range(n):
        if tmp[j] < min:  # 현재 위치의 값이 최소값보다 작은 경우, 최소값과 시작 지점 업데이트
            min = tmp[j]
            start_x = i
            start_y = j
        if tmp[j] > max:  # 현재 위치의 값이 최대값보다 큰 경우, 최대값과 종료 지점 업데이트
            max = tmp[j]
            end_x = i
            end_y = j
        board[i][j] = tmp[j]  # 등산 지도 정보 업데이트

check[start_x][start_y] = 1
cnt = 0
dfs(start_x, start_y)
print(cnt)