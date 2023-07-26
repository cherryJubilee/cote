# 중복가능
def dfs(L, sum):
    global res
    if L > res:
        return

    if sum > m: 
        return

    if sum == m:ㄴ
        if L < res:
            res = L # 이 부분 떄문에 지역변수로

    else:
        for i in kind:
            dfs(L+1, sum+kind[i])


n = int(input())
kind = list(map(int, input().split()))
m = int(input())
res = 21470000
kind.sort(reverse=True) # 내림차순, 가장 큰 동전부터 더하니까 효율적이다
dfs(0,0)

'''
res: 최소의 동전 개수를 저장하는 변수
최적의 해답을 찾고자 할 때, 
가능한 가장 적은 동전을 사용하는 방법을 찾는 것을 의미함.
res는 초기에 매우 큰 값(21470000)으로 설정되어 있어,
이보다 작은 동전 개수를 찾는 순간 res 값이 갱신됨.
'''

'''
 현재 탐색 경로(L)에서 사용한 동전의 개수가 
 이전까지 찾은 최소 동전 개수(res)보다 적을 경우, 최소 동전 개수를 
 현재 탐색 경로에서 사용한 동전의 개수로 갱신(res = L)하는 역할
'''