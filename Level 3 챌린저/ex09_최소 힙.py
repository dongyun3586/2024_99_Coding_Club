# https://www.acmicpc.net/problem/1927
import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())
A = []

for _ in range(n):
    v = int(input())
    if v == 0:
        if A:
            print(heappop(A))
        else:
            print(v)
    else:
        heappush(A, v)
