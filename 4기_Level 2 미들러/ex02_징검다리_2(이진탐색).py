# https://www.acmicpc.net/problem/11561
import sys
import math

input = sys.stdin.readline


def max_step(n):
    left, right = 1, int(math.sqrt(2 * n)) + 1  # 초기 범위 설정
    answer = 0

    while left <= right:
        mid = (left + right) // 2  # 현재 범위에서 중간값을 k로 설정
        sum_distance = mid * (mid + 1) // 2  # k까지의 누적합 계산: k(k+1)//2

        if sum_distance <= n:
            answer = mid  # 현재 mid 값을 저장
            left = mid + 1  # 더 큰 k 값을 탐색하기 위해 left를 mid + 1로 업데이트
        else:  # mid까지의 점프 누적합이 N을 초과하므로, mid가 점프 횟수로 불가능하다는 의미
            right = mid - 1  # 따라서 k 값을 줄여야 하므로, right = mid - 1로 설정하여 right를 왼쪽으로 옮기고, 더 작은 k 값을 탐색

    return answer


# 테스트 케이스 처리
t = int(input())
for _ in range(t):
    n = int(input())
    print(max_step(n))
