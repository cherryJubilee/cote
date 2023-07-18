from collections import deque

def solution(prices):
    prices = deque(prices)
    result = []

    while prices:
        check = prices.popleft()
        cnt = 0
        for price in prices:
            cnt += 1
            if check > price:  
                break  
        result.append(cnt)

    return result
