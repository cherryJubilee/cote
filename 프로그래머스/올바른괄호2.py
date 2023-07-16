"""
채점 결과
정확성: 69.5
효율성: 30.5
"""
from collections import deque


def solution(s):
    stack = deque()
    for i in s:
        # 만약 "(" 라면 일단 push
        if i == "(":
            stack.append(i)
        # 만약 ")" 이고
        elif i == ")":
            # 스택이 비어있다면 바로 false (3번째 입력 예시)
            if not stack:
                return False
            # 스택에 무언가가 있다면 pop
            else:
                stack.pop()
    if not stack:
        return True
    else:
        return False
