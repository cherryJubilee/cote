def solution(s):
    
    # 문자열을 정수형으로 변경
    s = list(map(int, s.split(" ")))
    result = f"{min(s)} {max(s)}"
    return result
    