
matrix = []    
for _ in range(101):
    temp = []
    for _ in range(101):
        temp.append(0)
    matrix.append(temp)


N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    for _x in range(x, x+10):
        for _y in range(y, y+10):
            matrix[_x][_y] = 1  

total = 0
for line in matrix:
    total += sum(line)

print(total)