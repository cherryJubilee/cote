def solution(arr):
    answer = [] 
    prev = arr[0] //기준
    for i in range(len(arr)):
        if arr[i] == prev:
            continue
        else:
            answer.append(prev)
            prev = arr[i]
    answer.append(prev)       
    return answer