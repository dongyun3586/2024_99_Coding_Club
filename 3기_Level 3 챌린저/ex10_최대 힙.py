# https://www.acmicpc.net/problem/11279

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())    # 연산의 개수
nums = []
for _ in range(n):
    v = int(input())
    if v > 0:
        heappush(nums, -v)
    elif nums:
        print(-heappop(nums))
    else:
        print(0)