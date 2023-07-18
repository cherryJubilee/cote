def solution(numbers):

    sum = 0
    for i in range(0, 10):
        sum += i
        
    num_sum = 0
    for i in numbers:
        num_sum += i
        
    num_sum = sum - num_sum 
    return num_sum
    