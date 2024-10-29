# https://school.programmers.co.kr/learn/courses/30/lessons/12914

def solution(n):
    # DP 테이블 초기화
    dp = [0] * (n + 1)

    # Bace Case 설정
    dp[1] = 1       # 첫 번째 칸에 도달하는 방법은 1칸을 뛰는 방법밖에 없으므로 1
    if n > 1:       # n이 1인 경우 dp[2] = 2를 시도하면 인덱스 에러가 발생함.
        dp[2] = 2   # 두 번째 칸에 도달하는 방법은 (1칸, 1칸)과 (2칸) 두 가지

    # 점화식을 이용하여 n까지의 경우의 수를 계산하여 DP 테이블을 채움.
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567

    return dp[n]


if __name__ == "__main__":
    print(solution(3))      # 3
    print(solution(4))      # 5
    print(solution(5))      # 8