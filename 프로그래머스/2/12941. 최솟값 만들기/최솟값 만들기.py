def solution(A,B):
    
    # 최솟값을 구하는 문제이니까 A는 오름차순 B는 내림차순으로 정렬해서 그나마 최소 되게 만들기.
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += (A[i] * B[i]) 
    return answer