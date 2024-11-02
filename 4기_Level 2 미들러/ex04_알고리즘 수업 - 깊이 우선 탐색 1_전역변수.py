# https://www.acmicpc.net/problem/24479
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)

for i in range(1, n + 1):
    graph[i].sort()

# 전역 변수로 count 관리
count = 1

def dfs(graph, v, visited):
    global count
    visited[v] = True
    result[v] = count
    count += 1
    for w in graph[v]:
        if not visited[w]:
            count = dfs(graph, w, visited)
    return count


visited = [False] * (n + 1)
result = [0] * (n+1)
dfs(graph, r, visited)

for i in result[1:]:
    print(i)