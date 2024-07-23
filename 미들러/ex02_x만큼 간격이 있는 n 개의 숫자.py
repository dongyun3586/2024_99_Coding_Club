# https://school.programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    answer = [x * i for i in range(1, n + 1)]
    return answer


if __name__ == "__main__":
    print(solution(2, 5))
    print(solution(4, 3))
    print(solution(-4, 2))
