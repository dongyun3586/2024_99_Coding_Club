# https://www.acmicpc.net/problem/14916

n = int(input())  # 거스른돈 액수


def min_coins(n):
    # 5원 동전의 최대 개수부터 시작하여 하나씩 줄여가면서 검사
    for five_count in range(n // 5, -1, -1):
        remaining = n - (5 * five_count)
        if remaining % 2 == 0:
            two_count = remaining // 2
            return five_count + two_count
    return -1   # # 만약 2원과 5원으로 거슬러 줄 수 없는 경우


print(min_coins(n))
