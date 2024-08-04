# https://school.programmers.co.kr/learn/courses/30/lessons/43238
"""이진 탐색으로 문제 해결"""
def solution(n, times):
    # 이진 탐색을 위한 변수 설정
    # 최소 시간(left): 심사관 한 명이 한 명을 심사하는 데 걸리는 가장 짧은 시간 min(times).
    # 최대 시간(right): 모든 사람이 가장 느린 심사관에게 심사를 받을 경우의 시간 max(times) * n.
    left, right = 1, max(times) * n

    while left < right:
        # 중간 시간(mid)을 계산하여 그 시간 안에 모든 사람이 심사를 받을 수 있는지 확인
        mid = (left + right) // 2
        total = 0

        # 각 심사관이 mid 시간 동안 처리할 수 있는 최대 사람 수를 합산
        for time in times:
            total += mid // time    # 모든 심사관의 처리 가능 인원 수 합산

        # 총 처리 가능한 사람 수와 n을 비교하여 이진 탐색의 방향 결정
        if total >= n:
            right = mid  # 시간이 충분하면, right를 줄여서 더 작은 시간도 가능한지 확인
        else:
            left = mid + 1  # 시간이 부족하면, left를 늘려서 더 많은 시간을 허용

    return left     # 이진 탐색이 종료되면 최소 시간을 반환


# 목표: 모든 사람이 심사를 받는 데 걸리는 최소 시간을 찾는 것
# 핵심: 시간이 정해졌을 때, 그 시간 안에 모든 사람이 심사를 받을 수 있는지를 확인하는 것
if __name__ == "__main__":
    print(solution(6, [7, 10]))     # 28