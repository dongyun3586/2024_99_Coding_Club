# https://www.acmicpc.net/problem/1135
from collections import deque


def bfs(graph, start):
    global level
    visited = [False] * len(graph)  # 각 노드의 방문 여부 기록
    queue = deque([(start, 0)])  # 시작 노드와 level을 큐에 추가
    visited[start] = True  # 시작 노드 방문처리

    while queue:
        v, level = queue.popleft()  # 큐에서 노드와 level을 꺼냄

        # 현재 노드에 인접한 노드를 탐색
        for i, w in enumerate(graph[v]):
            if not visited[w]:
                queue.append((w, level + 1 + i))  # 인접 노드를 큐에 추가
                visited[w] = True  # 방문 처리
    return level


n = int(input())
numbers = list(map(int, input().split()))   # -1 0 0
graph = [[] for _ in range(n)]

for i, num in enumerate(numbers[1:], start=1):
    graph[num].append(i)



# graph = [[1, 2],
#          [3, 4],
#          [5, 6],
#          [],
#          [],
#          [],
#          []]

# BFS 호출
print(bfs(graph, 0))
