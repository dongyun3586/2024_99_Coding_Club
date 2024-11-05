# https://www.acmicpc.net/problem/7562
import sys
from collections import deque

input = sys.stdin.readline

# 나이트의 이동 가능한 8가지 방향
directions = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (1, 2), (-1, -2), (1, -2)]


def bfs(start, dest, board_size):
    visited = [[False] * board_size for _ in range(board_size)]
    visited[start[0]][start[1]] = True
    queue = deque([(*start, 0)])

    while queue:
        x, y, count = queue.popleft()
        if (x, y) == dest:
            return count

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < board_size and 0 <= ny < board_size and not visited[nx][ny]:
                queue.append((nx, ny, count + 1))
                visited[nx][ny] = True


n = int(input())  # 테스트 케이스의 개수
for _ in range(n):
    w = int(input())  # 체스판의 한 변의 길이
    start = tuple(map(int, input().split()))    # 나이트의 시작 위치
    dest = tuple(map(int, input().split()))     # 나이트의 목적지 위치
    print(bfs(start, dest, w))
