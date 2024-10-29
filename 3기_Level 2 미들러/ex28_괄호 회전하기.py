# https://school.programmers.co.kr/learn/courses/30/lessons/76502
from collections import deque


def solution(s):
    answer = 0
    mapping = {')': '(', ']': '[', '}': '{'}
    stack = []
    s = deque(s)

    for i in range(len(s)-1):
        for char in s:
            if char in mapping:
                if stack and stack.pop() == mapping[char]:
                    continue
                else:
                    break
            else:
                stack.append(char)  # 여는 괄호일 경우 스택에 push
        else:
            answer = answer if stack else answer + 1

        # 문자열 회전
        s.append(s.popleft())

    return answer


if __name__ == '__main__':
    print(solution("[](){}"))  # 3
    print(solution("}]()[{"))  # 2
    print(solution("[)(]"))  # 0
    print(solution("}}}"))  # 0
