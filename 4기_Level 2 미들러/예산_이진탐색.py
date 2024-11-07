# https://www.acmicpc.net/problem/2512
def calculate_budget(requests, cap):
    total = 0
    for request in requests:
        total += min(request, cap)
    return total    # 총 배정 예산


def find_max_budget(N, requests, M):
    left, right = 0, max(requests)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        allocated_budget = calculate_budget(requests, mid)

        if allocated_budget <= M:  # 총 배정 예산이 예산 총액(M) 이하이면, 상한액을 높여 탐색
            answer = mid  # 가능한 상한액 후보
            left = mid + 1
        else:  # 총 배정 예산이 예산 총액(M)을 초과하면, 상한액을 낮춰 탐색
            right = mid - 1

    return answer


# 입력
N = int(input())  # 지방 수
requests = list(map(int, input().split()))  # 각 지방의 예산 요청
M = int(input())  # 총 예산

# 상한액 계산
print(find_max_budget(N, requests, M))
