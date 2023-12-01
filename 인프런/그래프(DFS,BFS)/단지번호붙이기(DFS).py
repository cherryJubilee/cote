# 1 -> 집이있는 곳 / 0 -> 집이 없는 곳
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    global cnt
    # 집을 발견하자마자 넘어 왔으므로 cnt += 1
    cnt += 1
    board[x][y] = 0  # 카운트 한 곳은 0으로 되돌려 두기
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
    if 0<=xx<n and 0<=yy<n and board[xx][yy] == 1:
        dfs(xx, yy)



n = int(input())
board = [list(map(int, input())) for _ in range(n)]
answer = [] #[각 단지별 집의 수 append]
# 첫번째 1을 찾아 가기
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:  # 집을 발견함!!!
            cnt = 0  # 집을 발견 할 때마다 0으로 초기화 하기, 그래야 다음 단지의 집을 셀때 1(처음)부터 시작할 수있다.
            dfs(i, j)
            # 저 def 쪽에서 구해진 집의 개수 = cnt를 answer에 append 해주기
            answer.append(cnt)



print(len(answer))
answer.sort()
for x in answer:
    print(x)

         


              