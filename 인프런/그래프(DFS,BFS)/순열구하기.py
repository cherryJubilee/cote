def dfs(L):
    global cnt
    if L == m:
        for j in range(m): # L,m 둘 다 상관없
            print(res[j], end=" ")
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if ckeck[i] == 0:
                check[i] = 1
                res[L] = i
                dfs(L+1)
                ckeck[i] = 0

n, m = map(int, input().split())
res = [0] * m   # 소스코드에는 n인데 m이 맞는것 같음 
check = [0] * (n+1)
cnt = 0
dfs(0)
print(cnt)

