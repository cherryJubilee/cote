import sys

def dfs(L, sum):
    if sum > total // 2:
        return
    if L==n:
        if sum == (total-sum):
            print("YES")
            sys.exit(0)


    else:
        dfs(L+1, sum + a[L])
        dfs(L+1, sum)


if __name__ == "__main__":
    n = int(input())  # 6
    a = list(map(int, input().split())) # 1 3 5 6 7 10
    total = sum(a)
    dfs(0,0)
    
