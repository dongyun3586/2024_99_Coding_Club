# https://school.programmers.co.kr/learn/courses/30/lessons/12914

def solution(n):
    # 메모이제이션을 위한 배열 초기화
    memo = [-1] * (n + 1)

    def dfs(k):
        # base case
        if k == 1:
            return 1
        if k == 2:
            return 2

        # 이미 계산된 경우 바로 반환
        if memo[k] != -1:
            return memo[k]

        # 재귀 호출을 통한 계산
        memo[k] = (dfs(k - 1) + dfs(k - 2)) % 1234567
        return memo[k]

    return dfs(n)


if __name__ == "__main__":
    print(solution(3))      # 3
    print(solution(4))      # 5
    print(solution(5))      # 8