def solution(s):
    
    s = list(map(int, s.split(" ")))
    ans = f'{min(s)} {max(s)}'
    return ans
    