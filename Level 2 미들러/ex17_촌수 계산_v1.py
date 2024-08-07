# https://www.acmicpc.net/problem/2644
# 여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성
import sys
input = sys.stdin.readline

n = int(input())  # 전체 사람의 수
a, b = map(int, input().split())  # 촌수를 계산해야 하는 서로 다른 두 사람의 번호
m = int(input())  # 부모 자식들 간의 관계의 개수
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(v, count):
    global chonsu
    visited[v] = True
    if v == b:
        chonsu = count
        return

    for w in graph[v]:
        if not visited[w]:
            dfs(w, count+1)

chonsu = -1
visited = [False] * (n + 1)
dfs(a, 0)
print(chonsu)
