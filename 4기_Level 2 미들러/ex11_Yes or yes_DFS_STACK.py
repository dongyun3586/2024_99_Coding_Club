# https://www.acmicpc.net/problem/25195
import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # 정점의 수, 간선의 수

# 정방향 그래프 생성
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

k = int(input())  # 팬클럽 수
fanclub_nodes = set(map(int, input().split()))  # 팬클럽이 있는 정점의 번호

def iterative_dfs(graph, start):
    stack = [start]
    visited = [False] * (n + 1)

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True

            if v in fanclub_nodes:
                continue

            # 현재 노드가 리프 노드이면
            if not graph[v]:
                return False

            # 현재 노드에서 이동할 수 있는 모든 노드를 스택에 추가
            for w in graph[v]:
                if not visited[w]:
                    stack.append(w)
    return True


if iterative_dfs(graph, 1):
    print("Yes")
else:
    print("yes")