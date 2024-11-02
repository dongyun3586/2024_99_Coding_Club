# https://www.acmicpc.net/problem/24444
import sys
from collections import deque

input = sys.stdin.readline

n, m, r = map(int, input().split())  # 정점의 수, 간선의 수, 시작 정점
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)

# 각 정점의 인접 정점 목록을 오름차순으로 정렬
for i in graph:
    i.sort()

def bfs(graph, start):
    visited = [False] * (n + 1)
    visited[start] = True
    queue = deque([start])

    result = [0] * (n + 1)
    count = 1

    while queue:
        v = queue.popleft()
        result[v] = count
        count += 1
        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                queue.append(w)
    return result


result = bfs(graph, r)
for i in result[1:]:
    print(i)
