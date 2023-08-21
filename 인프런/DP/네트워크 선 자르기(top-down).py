'''
네트워크 선을 1m, 2m의 길이를 갖는 선으로 자르려고 한다.
'''

def dfs(len):
    # 커트를 해줘야 함. 이미 있는 값 이라면,
    # 있는거 그대로 리턴 해줘라(더이상 가지치지 말고)
    if dy[len] > 0:
        return dy[len]
    #도착점
    if len == 1 or len == 2:
        # 당연히 dfs(1) = 1, dfs(2) = 2
        return len
    else:
        # memoryzation: dy[len] == dfs(len)
        dy[len] = dfs(len-1) + dfs(len-2)
        return dy[len]

n = int(input())
dy = [0] * (n+1)
print(dfs(n))



