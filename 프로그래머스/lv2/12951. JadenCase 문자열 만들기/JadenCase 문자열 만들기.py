def solution(s):
    s = s.split(" ") 
    answer = []

    for i in s:
        # 문자열 i가 비어있지 않다면
        if len(i) > 0:
            # 첫 문자가 알파벳이라면
            if i[0].isalpha():
                i = i[0].upper() + i[1:].lower()
                answer.append(i)
            # 첫 문자가 알파벳이 아니라면
            else: 
                i = i[0] + i[1:].lower()
                answer.append(i)
        else:
            answer.append(i)

    result = " ".join(answer)
    return result
