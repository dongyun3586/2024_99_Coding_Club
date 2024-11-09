# https://www.acmicpc.net/problem/25195

### 엄청 오래 걸림 ###
from collections import deque
import sys
input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())  # 정점 수, 간선 수

# 정방향 그래프 및 역방향 그래프 생성
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 팬클럽 노드 입력 받기
s = int(input())  # 팬클럽 곰곰이가 존재하는 정점의 개수
fan_club_nodes = set(map(int, input().split()))


def bfs(graph, fan_club_nodes, start):
    visited = [False] * (n + 1)
    visited[start] = True
    queue = deque([start])
    if start in fan_club_nodes:
        return True

    while queue:
        v = queue.popleft()
        if not graph[v]:
            return False

        for w in graph[v]:
            if w not in fan_club_nodes and not visited[w]:
                visited[w] = True
                queue.append(w)
    return True


# 도달 가능한 노드가 팬클럽 노드에 모두 포함되는지 확인
if bfs(graph, fan_club_nodes, 1):
    print("Yes")
else:
    print("yes")
