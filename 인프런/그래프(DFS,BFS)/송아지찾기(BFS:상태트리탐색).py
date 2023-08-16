# 최소 몇번의 점프로 송아지의 위치까지 가는지
from collections import deque

max = 10000 # 직선의 좌표 점은 1부터 10,000 까지이다.
distance = [0] * (max+1)
check = [0] * (max+1)
n,m = map(int, input().split()) # 현수의 위치n, 송아지 위치m 
check[n] = 1  # 현수의 현재 위치를 방문했다고 체크
distance[n] = 0  # 현수의 현재 위치까지의 점프 수는 0

dQ = deque()  # BFS를 위한 큐
dQ.append(n)  # 현수의 현재 위치를 큐에 추가

# BFS 알고리즘 시작
while dQ:
    now = dQ.popleft()  # 현재 위치를 큐에서 꺼냄
    for next in (now-1, now +1, now+5):  # 현재 위치에서 이동 가능한 다음 위치를 확인
        if 0 < next <= max:  # 이동할 위치가 1부터 10000 사이에 있는지 확인
            if check[next] == 0:  # 아직 이동할 위치를 방문하지 않았다면
                dQ.append(next)  # 큐에 이동할 위치 추가
                check[next] = 1  # 이동할 위치를 방문했다고 체크
                distance[next] = distance[now] + 1  # 이동할 위치까지의 점프 수 갱신
# BFS 알고리즘 끝

print(distance[m])  # 송아지의 위치까지의 최소 점프 수 출력