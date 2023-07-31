from itertools import permutations

def solution(numbers):
    
    num_ls = []
    for i in range(1, len(numbers)+1):
        for num in permutations(numbers, i):
            num_ls.append(int(''.join(num)))
            
    num_ls = set(num_ls)        
    cnt = 0
    for num_str in num_ls:  
        if num_str > 1:         
            for i in range(2, int(num_str**0.5) + 1):
                if num_str % i == 0:
                    break
            else:
                cnt += 1
    return cnt
                
            

        
        