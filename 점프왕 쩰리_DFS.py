# https://www.acmicpc.net/problem/16173
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]


def dfs(x, y):
    visited[x][y] = True

    if A[x][y] == -1:
        return True

    for dx, dy in [(x + A[x][y], y), (x, y + A[x][y])]:
        if 0 <= dx < N and 0 <= dy < N and not visited[dx][dy]:
            if dfs(dx, dy):
                return True

    return False


visited = [[False] * N for _ in range(N)]
if dfs(0, 0):
    print("HaruHaru")
else:
    print("Hing")
