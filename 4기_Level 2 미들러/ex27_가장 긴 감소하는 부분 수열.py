# https://www.acmicpc.net/problem/11722
n = int(input())  # 수열의 크기
arr = list(map(int, input().split()))  # 수열 값


def longest_decreasing_subsequence(n, arr):
    dp = [1] * n  # 초기값: 모든 원소는 최소 길이 1의 수열을 가짐

    # DP 배열 계산
    for i in range(n):
        for j in range(i):
            if arr[j] > arr[i]:  # 감소하는 조건
                dp[i] = max(dp[i], dp[j] + 1)

    # 가장 긴 감소하는 부분 수열의 길이 반환
    return max(dp)


print(longest_decreasing_subsequence(n, arr))
