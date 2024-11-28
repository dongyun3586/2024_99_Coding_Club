# https://www.acmicpc.net/problem/11054
def longest_bitonic_subsequence(N, A):
    # 증가 부분 수열(LIS)
    LIS = [1] * N
    for i in range(N):
        for j in range(i):
            if A[j] < A[i]:
                LIS[i] = max(LIS[i], LIS[j] + 1)

    # 감소 부분 수열(LDS)
    LDS = [1] * N
    for i in range(N - 1, -1, -1):
        for j in range(i + 1, N):
            if A[j] < A[i]:
                LDS[i] = max(LDS[i], LDS[j] + 1)

    # 바이토닉 수열의 최대 길이 계산
    max_length = 0
    for i in range(N):
        max_length = max(max_length, LIS[i] + LDS[i] - 1)

    return max_length


# 입력 처리
N = int(input())
A = list(map(int, input().split()))
print(longest_bitonic_subsequence(N, A))
