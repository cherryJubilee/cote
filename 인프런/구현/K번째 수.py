# K번째 수

'''

n,s,e,k
s번째부터 e번째 까지의 수를 오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력
'''
T = int(input())

for a in range(T):
    n,s,e,k = map(int, input().split())
    num_list = list(map(int, input().split()))
    num_list = num_list[s-1:e]
    num_list.sort()
    print(f'#{a+1} {num_list[k-1]}')
    
