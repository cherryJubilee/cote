dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):
    check[x][y] = 1
    if x == 0:
        print(y)
    else:
        # 왼쪽
        if y-1>=0 and board[x][y-1]==1 and check[x][y-1]==0:
            dfs(x, y-1)
        # 오른쪽
        elif y+1<10 and board[x][y+1]==1 and check[x][y+1]==0:
            dfs(x, y+1)       
        # 위
        else:
            dfs(x-1, y)




board = [list(map(int, input().split())) for _ in range(10)]
# 체크배열 만들기
check = [[0] * 10 for _ in range(10)]
# 뒤(목적지 = 2)에서 부터 타고 올라가는 방식
for y in range(10):
    if board[9][y] == 2:
        dfs(9, y)