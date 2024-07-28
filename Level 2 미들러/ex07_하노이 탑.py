# https://school.programmers.co.kr/learn/courses/30/lessons/12946

def solution(n):
    answer = []

    def hanoi(n, source, target, temp):
        if n == 1:
            answer.append([source, target])
            return
        hanoi(n - 1, source, temp, target)
        answer.append([source, target])
        hanoi(n - 1, temp, target, source)

    hanoi(n, 1, 3, 2)
    return answer


if __name__ == "__main__":
    print(solution(2))  # [[1, 2], [1, 3], [2, 3]]
    print(solution(3))
