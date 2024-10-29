# https://www.acmicpc.net/problem/11561
import sys
input = sys.stdin.readline


def max_step(stones):
    current_sum_distance = 0    # 현재까지의 누적 거리
    jumps = 0                   # 점프 횟수
    jump_distacne = 1           # 현재 점프할 거리

    # 징검다리의 개수 내에서 계속 점프
    while current_sum_distance + jump_distacne <= stones:
        current_sum_distance += jump_distacne   # 누적 거리 업데이트
        jumps += 1              # 점프 횟수 증가
        jump_distacne += 1      # 다음 점프 거리 1 증가

    return jumps


# 테스트 케이스 처리
t = int(input())
for _ in range(t):
    n = int(input())
    print(max_step(n))
