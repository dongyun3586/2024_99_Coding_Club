# https://www.acmicpc.net/problem/31926

def solution(n):
    result = 0
    while n > 1:
        n //= 2
        result += 1
    return result + 10


n = int(input())
print(solution(n))