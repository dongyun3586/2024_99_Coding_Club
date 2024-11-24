# https://www.acmicpc.net/problem/11055
# 입력 처리
n = int(input())
A = list(map(int, input().split()))

# DP 배열 초기화
dp = A[:]  # 각 원소를 자기 자신으로 초기화

# DP 점화식 적용
for i in range(1, n):
    for j in range(i):
        if A[j] < A[i]:  # 증가하는 부분 수열 조건
            dp[i] = max(dp[i], dp[j] + A[i])

# 결과 출력
print(max(dp))  # dp 배열의 최대값이 정답
