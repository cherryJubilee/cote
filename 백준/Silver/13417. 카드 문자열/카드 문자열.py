# [13417] 카드문자열
from collections import deque
T = int(input())

for _ in range(T):
    num = int(input())  # 5
    cards = list(input().split())  # ['A', 'S ', 'D',  'F',  'G']
    # print(cards)

    q = deque()
    q.append(cards[0])
    standard = cards[0]  # 기준

    for i in range(1, num):

        if standard >= cards[i]:
            q.appendleft(cards[i])
            standard = cards[i]
        else:
            q.append(cards[i])

    print("".join(q))

