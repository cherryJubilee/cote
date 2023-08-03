def solution(numbers, target):   
    return dfs(0, 0, numbers, target)
    
def dfs(level, sum, numbers, target):
    if level == len(numbers):
        if sum == target:
            return 1
        else:
            return 0
    else:
        return dfs(level+1, sum + numbers[level], numbers, target) + dfs(level+1, sum - numbers[level], numbers, target)
