def solution(n):
    answer = 0
    ternary = []

    while n > 0:
        ternary.append(n % 3)
        n = n // 3
    
    for i in range(len(ternary)):
        answer += ternary[i] * (3 ** (len(ternary) - 1 - i))
        
    return answer
