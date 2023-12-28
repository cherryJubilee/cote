cnt = 0
def solution(numbers, target):
    dfs(0, 0, numbers, target)
    return cnt
    
    
def dfs(level, current_sum, numbers, target):
    
    global cnt 
    if level == len(numbers):
        if current_sum == target:
            cnt += 1
    else:
        dfs(level+1, current_sum + numbers[level], numbers, target)
        dfs(level+1, current_sum - numbers[level], numbers, target)


        
