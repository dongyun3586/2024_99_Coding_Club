# https://www.acmicpc.net/problem/16173
from collections import deque

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

def bfs(start):
    visited = [[False] * N for _ in range(N)]
    queue = deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()
        if A[x][y] == -1:
            return "HaruHaru"
        for dx, dy in [(x+A[x][y], y), (x, y+A[x][y])]:
            if 0<= dx < N and 0<= dy < N and not visited[dx][dy]:
                visited[dx][dy] = True
                queue.append((dx, dy))

    return "Hing"


print(bfs((0, 0)))