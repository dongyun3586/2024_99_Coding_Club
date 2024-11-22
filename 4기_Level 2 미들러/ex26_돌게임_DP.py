# https://www.acmicpc.net/problem/9655

n = int(input())


def stone_game(n):
    # DP 테이블 초기화
    dp = [False] * (n + 3)

    # 초기값 설정
    dp[1] = True    # SK 승리
    dp[2] = False   # CY 승리
    dp[3] = True    # SK 승리

    # 점화식을 이용하여 DP 테이블 채우기
    for i in range(4, n + 1):
        dp[i] = not (dp[i - 1] and dp[i - 3])

    # 결과 출력
    return "SK" if dp[n] else "CY"

print(stone_game(n))