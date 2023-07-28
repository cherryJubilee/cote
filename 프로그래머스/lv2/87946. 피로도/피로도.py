from itertools import permutations
def solution(k, dungeons):
    
    answer = 0
    for p in permutations(dungeons, len(dungeons)):
        
        first = k
        cnt = 0
        
        for before_fatigue, fatigue in p:
            if first >= before_fatigue:
                first -= fatigue
                cnt += 1
                
        answer = max(answer, cnt)
                
    return answer
            
    
    