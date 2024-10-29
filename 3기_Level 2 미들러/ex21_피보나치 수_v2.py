# https://school.programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    dp = [0] * (n+1)        # dp 테이블 생성
    dp[0], dp[1] = 0, 1     # base case 설정

    # 피보나치 수 계산
    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567

    # n번째 피보나치 수를 반환
    return dp[n]


if __name__ == '__main__':
    print(solution(3))      # 2
    print(solution(5))      # 5