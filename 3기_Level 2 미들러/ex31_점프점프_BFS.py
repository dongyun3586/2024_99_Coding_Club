# https://www.acmicpc.net/problem/14248
from collections import deque


def bfs(start):
    visited = [False] * n   # 방문 리스트 초기화
    visited[start] = True
    queue = deque([start])
    count = 1

    while queue:
        current = queue.popleft()

        # 왼쪽으로 점프
        left = current - distances[current]
        if left >= 0 and not visited[left]:
            visited[left] = True
            queue.append(left)
            count += 1

        # 오른쪽으로 점프
        right = current + distances[current]
        if right < n and not visited[right]:
            visited[right] = True
            queue.append(right)
            count += 1

    return count


n = int(input())    # 돌다리의 돌 개수
distances = list(map(int, input().split()))     # 점프 거리 리스트
start = int(input()) - 1    # 출발점 (0-index로 변환)

# BFS를 이용하여 방문 가능한 돌들의 개수 출력
print(bfs(start))   # dfs(2)