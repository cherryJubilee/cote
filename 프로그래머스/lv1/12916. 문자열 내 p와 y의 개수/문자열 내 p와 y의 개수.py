def solution(s):
    answer = 0
    s = s.lower()
    
    for i in s:
        if i == "p":
            answer += 1
        elif i == "y":
            answer -= 1
        else:
            continue
        
    if answer == 0:
        return True
    else:
        return False