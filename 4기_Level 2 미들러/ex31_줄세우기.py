# https://www.acmicpc.net/problem/2631
import sys

input = sys.stdin.readline

n = int(input())
children = [int(input()) for _ in range(n)]


def minimum_moves_to_sort(n, children):
    # dp[i]: i번째 원소를 끝으로 하는 LIS의 최대 길이
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if children[j] < children[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    # LIS 길이 계산
    lis_length = max(dp)

    # 최소 이동 수 = 전체 길이 - LIS 길이
    return n - lis_length


# 최소 이동 수 출력
print(minimum_moves_to_sort(n, children))
