import sys
'''
중요!
만약 현재까지 선택한 바둑이들의 무게의 합(sum)과 
앞으로 고려할 바둑이들의 무게의 합(total - tsum)을 더한 값이 
현재까지 찾은 최대 무게(result)보다 작다면, 
이후에 어떤 바둑이를 선택하더라도 현재까지 찾은 최대 무게를 넘지 못함
'''

# sum: 내가 만드는 부분집합의 합
def dfs(L, sum, tsum):  # L: 각각의 바둑이의 weights리스트에 접근 하기 위한 index
    global result

    if sum + (total - tsum) < result: # 더 좋은 답이 안나온다는 의미
        return
    if sum > c:
        return

    if L == n: # 부분 집합 한 개가 완성
        if sum > result:
            result = sum

    else:
        dfs(L+1, sum+weights[L], tsum+weights[L])
        dfs(L+1, sum, tsum+weights[L])


c, n = map(int, input().split())
weights = [0] * n
result = -2147000000 # 가장 큰 값을 찾는 거니까 아주 작은 값을 아무거나 넣어두기(초기화)
for i in range(n):
    weights[i] = int(input())
    
total = sum(weights)
dfs(0,0,0)

'''
sum: 지금까지 "선택"한 바둑이 무게
tsum:ㅠ현재까지 "고려"된 모든 바둑이 무게
total: 현재까지 바둑이 총 무게
result: 현재까지 찾은 바둑이 최대 무게
'''