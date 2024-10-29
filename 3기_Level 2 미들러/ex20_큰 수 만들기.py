# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    stack = []  # 결과를 저장할 스택
    for num in number:
        # 스택의 마지막 값이 현재 값보다 작으면 스택에서 제거 (k번 수행 가능)
        while k and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    # 만약 아직 제거할 숫자가 남았다면, 스택의 뒤에서부터 제거
    if k > 0:
        stack = stack[:-k]

    # 스택에 남아있는 숫자들을 합쳐서 반환
    return ''.join(stack)


if __name__ == "__main__":
    print(solution("1924", 2))  # "94
    print(solution("1231234", 3))  # "3234"
    print(solution("4177252841", 4))  # "775841"
    print(solution("999", 1))  # 99
