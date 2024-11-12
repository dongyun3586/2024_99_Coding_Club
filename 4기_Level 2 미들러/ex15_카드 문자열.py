# https://www.acmicpc.net/problem/13417
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    m = int(input())
    arr = list(input().split())
    s = deque(arr[0])
    for c in arr[1:]:
        if c <= s[0]:
            s.appendleft(c)
        else:
            s.append(c)
    print(''.join(s))
