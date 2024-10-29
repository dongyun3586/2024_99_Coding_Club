# https://www.acmicpc.net/problem/1389
import sys
from math import inf
input = sys.stdin.readline


#입력 받기
n, m = map(int, input().split())    # 유저의 수, 친구 관계의 수
user = [[inf] * (n + 1) for _ in range(n + 1)]  # 유저 간 최단 거리를 저장하는 2차원 리스트

# 친구 관계 입력 받기
for i in range(m):
    a, b = map(int, input().split())
    user[a][b] = 1
    user[b][a] = 1

# 플로이드-워셜 알고리즘 수행
for k in range(1, n + 1):
    user[k][k] = 0  # 자기자신의 거리는 0으로 설정
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            user[i][j] = min(user[i][j], user[i][k] + user[k][j])

# 최소 케빈 베이컨 수를 가지는 유저 찾기
min_bacon_sum = inf
min_user = -1   # 케빈 베이컨 수가 최소인 유저의 번호 저장

# 각 유저에 대해 user[i][1:]의 합을 계산하여, 유저 i의 케빈 베이컨 수를 구한다.
for i in range(1, n + 1):
    bacon = sum(user[i][1:])    # i번째 유저의 케빈 베이컨 수
    if bacon < min_bacon_sum:
        min_bacon_sum = bacon
        min_user = i

print(min_user)
