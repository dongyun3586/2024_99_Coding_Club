# https://www.acmicpc.net/problem/1374
import sys
import heapq
from collections import deque
input = sys.stdin.readline


n = int(input())    # 강의의 수
visited = [False] * (n+1)
arr = deque()

for _ in range(n):
    num, start, end = map(int, input().split())     # 강의 번호, 시작 시간, 종료 시간
    arr.append((start, end, num))

arr.sort()    # 시작 시간으로 정렬
max_count = 0

heap = []
for _ in range(n):
    lecture = arr
    if heap:
        ...
    heapq.heappush(heap, arr[_])
