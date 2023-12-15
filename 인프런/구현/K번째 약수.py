'''
N의 약수들 중 K번째로 작은 수를 출력한다. 
만일 N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우에는 -1을 출
'''


n, k = map(int, input().split())
# 6, 3

'''
# 풀이1
divisor = [] # 약수 리스트
for i in range(1, n+1):
    if n % i == 0:
        divisor.append(i)

if k > len(divisor):
    print(-1)
else:
    divisor.sort()
    print(divisor[k-1])
'''

cnt = 0
for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
    if cnt == k: # 이게 참 이어야 break 하고 끝나는데, 거짓인 경우 else문으로 이동
        print(i)
        break
else:
    print(-1)



