# https://www.acmicpc.net/problem/2644
# 여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)


def bfs(start, target):
    queue = deque([start])
    visited = [0] * len(graph)

    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if not visited[w]:
                queue.append(w)
                visited[w] = visited[v] + 1

    return visited[target] if visited[target] > 0 else -1


print(bfs(a, b))
