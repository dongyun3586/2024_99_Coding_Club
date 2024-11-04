# https://www.acmicpc.net/problem/2644
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
start, target = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(graph, start, target):
    visited = [False] * (n + 1)
    visited[start] = True
    queue = deque([(start, 0)])
    while queue:
        u, chonsu = queue.popleft()
        if u == target:
            return chonsu
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append((v, chonsu + 1))

    return -1


print(bfs(graph, start, target))
