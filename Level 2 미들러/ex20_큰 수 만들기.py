# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    target_length = len(number) - k
    number = [i for i in number]
    stack = []
    for i in number:
        while stack and i > stack[-1] and k:
            stack.pop()
            k -= 1
        stack.append(i)
    while len(stack) > target_length:
         stack.pop()
    return ''.join(stack)


if __name__ == "__main__":
    print(solution("1924", 2))      # "94
    print(solution("1231234",3))    # "3234"
    print(solution("4177252841",4)) # "775841"
    print(solution("999", 1))       # 99