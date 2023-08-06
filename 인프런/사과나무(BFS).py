from collections import deque
dx = [-1,0,1,0] # 12시, 3시, 6시, 9시 순서
dy = [0,1,0,-1]

n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
a = []  
for i in range(n):  
    row = list(map(int, input().split()))  
    a.append(row) 

check = [[0] * n for _ in range(n)]
check[n//2][n//2] = 1
sum = 0
sum += a[n//2][n//2]
Q = deque()
Q.append((n//2, n//2))   # Q = (2,2) 튜플!!
level = 0

while True:
    if level == n//2:
        break
    size = len(Q)
    # 레벨탐색 시작
    for i in range(size):
        tmp = Q.popleft()  # popleft로 하나 꺼내서 4개 가지로 퍼지기
        for j in range(4): #12,3,6,9시 총 4개
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if check[x][y] == 0:
                sum += a[x][y]
                check[x][y] = 1
                Q.append((x,y))   # Q에 (1,2) (2,3) (3,2) (2,1)이 들어오게 됨

    level += 1
print(sum)
