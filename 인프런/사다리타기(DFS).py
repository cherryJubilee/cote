'''
사다리를 통해서 움직인다 사다리 = 1
맨 아래 행중 목적지 = 2 에서 부터 출발해서 위로 올라간다
사다리가 1이고 아직 다녀가지 않은 곳(체크 = 0) 이라면 움직인다.
출력 -> 행(x)가 0일때 열(y) 출력
'''
def dfs(x, y):
    # dfs가 호출되었으면 일단 check 배열 1로 바꿔주기
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

# 입력 받기
board = [list(map(int, input().split())) for _ in range(10)]
# 체크배열 만들기
check = [[0] * 10 for _ in range(10)]
# 뒤(목적지 = 2)에서 부터 타고 올라가는 방식
for y in range(10):
    if board[9][y] == 2:
        dfs(9, y)