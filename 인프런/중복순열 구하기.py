input = sys.stdin.readline # 대량으로 입력 읽어올 때
# s = input().rstrip();  # 문자열일 때만 씀


def dfs(L):
    global cnt
    if L == M:
        for j in range(m):
            print(res[j], end = " ")
        print()
        cnt+=1

    else:
       for i in range(1, n+1):
        res[L] = if
        dfs(L+1)



n, m = map(int, input().slpit())
res = [0] * m
cnt = 0
dfs(0)
print(cnt)