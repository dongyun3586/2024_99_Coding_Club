# https://www.acmicpc.net/problem/18352
import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())  # 도시의 개수, 도로의 개수, 거리, 출발 도시
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)


def bfs(start):
    visited = [False] * (n + 1)
    queue = deque([(start, 0)])
    visited[start] = True
    result = []

    while queue:
        v, dist = queue.popleft()
        if dist == k:
            result.append(v)
        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                queue.append((w, dist + 1))
    if result:
        result.sort()
        print('\n'.join(map(str, result)))
    else:
        print(-1)

bfs(x)
