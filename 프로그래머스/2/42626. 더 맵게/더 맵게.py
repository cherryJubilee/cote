import heapq 
def solution(scoville, K):
    
    heapq.heapify(scoville) # scoville를 힙으로 반환
        
    ans = 0
    while scoville[0] < K:
        ans += 1
        one_min= heapq.heappop(scoville) # scoville에서 가장 작은 값을 pop
        two_min= heapq.heappop(scoville) # scoville에서 가장 작은 값을 pop
        heapq.heappush(scoville, one_min + two_min * 2) # heap으로 push	
        
        if len(scoville) == 2 and (scoville[0] + scoville[1] * 2) < K:
            return -1
    return ans