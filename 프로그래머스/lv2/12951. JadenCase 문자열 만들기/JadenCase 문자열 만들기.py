def solution(s):
    
    s = s.split(" ") 
    answer = []
    
    #공백문자가 연속해서 나올 수 있다는거에 주의하자!!!
    # 참고 # "1qWe    eE ff"를 split(" ") 하면 ['1qWe', '', '', '', 'eE', 'ff']이렇게 된다
    # 빈문자열도 사용해야하니 for문 돌릴 때 추가해야함!!!
    
    for i in s:
        if i != "":
            # 알파벳 이라면
            if i[0].isalpha():
                i = i[0].upper() + i[1:].lower()
                answer.append(i)
            # 알파벳이 아니라면 
            else: 
                i = i[0] + i[1:].lower()
                answer.append(i)
        else:
            answer.append(i)
                
    result =  " ".join(answer)
    return result
            
        
    