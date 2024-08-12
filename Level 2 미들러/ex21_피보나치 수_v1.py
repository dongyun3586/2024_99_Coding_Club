# https://school.programmers.co.kr/learn/courses/30/lessons/12945
import sys
sys.setrecursionlimit(10**6)    #  재귀 깊이 늘리기


def solution(n):
    memo = {0: 0, 1: 1}   # 메모이제이션을 위한 딕셔너리, base case 저장

    def fibonacci(x):
        # 이미 계산된 값이 있으면 그 값을 반환
        if x in memo:
            return memo[x]

        # 새로운 피보나치 수 계산
        memo[x] = (fibonacci(x-1)+fibonacci(x-2))%1234567
        return memo[x]

    # 최종적으로 n번째 피보나치 수 반환
    return fibonacci(n)


if __name__ == '__main__':
    print(solution(3))      # 2
    print(solution(5))      # 5