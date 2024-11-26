# https://www.acmicpc.net/problem/9461
import sys
input = sys.stdin.readline


# 파도반 수열을 저장할 리스트
dp = [0] * 101
dp[1], dp[2], dp[3] = 1, 1, 1

# 점화식을 사용해 100까지의 파도반 수열 계산
for i in range(4, 101):
    dp[i] = dp[i-2] + dp[i-3]

test_case = int(input())
results = []

# 각 테스트 케이스 입력 및 결과 저장
for _ in range(test_case):
    n = int(input())
    results.append(dp[n])

# 결과 출력
print('\n'.join(map(str, results)))