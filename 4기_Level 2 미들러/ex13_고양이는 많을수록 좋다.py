# https://www.acmicpc.net/problem/27961

n = int(input())  # 고양이 수


def solution(n):
    if n < 2:
        return n
    count = 1
    total = 1
    while True:
        if total * 2 == n:
            return count + 1
        elif total * 2 > n:
            return count + 1
        total *= 2
        count += 1


print(solution(n))
