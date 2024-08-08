# https://www.acmicpc.net/problem/5547
from collections import deque


def bfs(y, x):
    queue = deque([(y, x)])
    visited[y][x] = 1
    cnt = 0

    while queue:
        y, x = queue.popleft()
        for dx, dy in directions[y % 2]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < H + 2 and 0 <= nx < W + 2:
                if board[ny][nx] == 1:
                    cnt += 1
                elif not visited[ny][nx]:
                    visited[ny][nx] = 1
                    queue.append((ny, nx))
    return cnt


# 입력 받기
W, H = map(int, input().split())
visited = [[0 for _ in range(W + 2)] for _ in range(H + 2)]
board = [[0 for _ in range(W + 2)] for _ in range(H + 2)]   # 패딩 추가
for i in range(1, H + 1):
    board[i][1:W+1] = list(map(int, input().split()))

# 홀수 행과 짝수 행에 대한 이동 좌표
directions = [
    [(-1, -1), (0, -1), (1, 0), (0, 1), (-1, 1), (-1, 0)],  # 홀수 행
    [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 0)]     # 짝수 행
]

# 외벽 길이 계산 결과 출력
print(bfs(0, 0))


"""
8 4
0 1 0 1 0 1 1 1
0 1 1 0 0 1 0 0
1 0 1 0 1 1 1 1
0 1 1 0 1 0 1 0

64
"""

"""
8 5
0 1 1 1 0 1 1 1
0 1 0 0 1 1 0 0
1 0 0 1 1 1 1 1
0 1 0 1 1 0 1 0
0 1 1 0 1 1 0 0

56
"""