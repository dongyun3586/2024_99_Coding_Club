# https://school.programmers.co.kr/learn/courses/30/lessons/43238?language=python3
def solution(n, times):
    left, right = 1, max(times) * n

    while left <= right:
        mid = (left + right) // 2
        count = 0   # 각 심사관이 mid 시간 동안 처리할 수 있는 최대 사람 수 저장

        for time in times:
            count += mid // time

        if count >= n:
            right = mid - 1
        else:
            left = mid + 1

    return left


if __name__ == '__main__':
    print(solution(6, [7, 10]))     # 28