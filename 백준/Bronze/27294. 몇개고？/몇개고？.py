# [27294] 몇개고?

T, S = map(int, input().split())

if (T <= 11 or T > 16) or S == 1:
    answer = 280
elif (12 <= T <= 16) and S == 0:
    answer = 320

print(answer)
