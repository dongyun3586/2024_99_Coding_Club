# https://school.programmers.co.kr/learn/courses/30/lessons/154539

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i in range(len(numbers)):
        while stack and numbers[i] > numbers[stack[-1]]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer


if __name__=="__main__":
    print(solution([2, 3, 3, 5]))           # [3, 5, 5, -1]
    print(solution([9, 1, 5, 3, 6, 2]))     # [-1, 5, 6, 6, -1, -1]