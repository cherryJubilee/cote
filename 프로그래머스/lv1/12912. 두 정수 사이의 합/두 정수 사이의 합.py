def solution(a, b):
    
    if a == b:
        return a
    elif b > a:
        sum = 0
        for i in range(a, b+1):
            sum += i
        return sum 
    else:
        sum = 0
        for i in range(b, a+1):
            sum += i
        return sum 
        