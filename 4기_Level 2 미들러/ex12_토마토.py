# https://www.acmicpc.net/problem/7569

import sys
from collections import deque
input = sys.stdin.readline


def bfs_tomato_ripening(M, N, H, boxes):
    queue = deque()
    directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]  # 3차원에서 위, 아래, 좌, 우, 앞, 뒤 여섯 방향 정의

    # 익은 토마토 위치 큐에 저장: 토마토가 익어있는 칸(값이 1)을 찾아 그 위치 (h, n, m)와 현재 일수 0을 queue에 추가한다.
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if boxes[h][n][m] == 1:
                    queue.append((h, n, m, 0))  # (높이, 행, 열, 날짜)

    max_days = 0    # max_days는 모든 토마토가 익기까지 걸린 최대 일수를 기록

    # BFS 수행: queue가 빌 때까지 BFS 탐색을 수행
    while queue:
        z, y, x, days = queue.popleft()
        max_days = max(max_days, days)

        # 인접한 6개 방향 탐색
        for dz, dy, dx in directions:
            nz, ny, nx = z + dz, y + dy, x + dx
            # 상자 범위 안에 있고, 아직 익지 않은 토마토(boxes[nz][ny][nx] == 0)인 경우 익은 토마토로 바꾸고, 일수를 하루 증가시켜 큐에 추가
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and boxes[nz][ny][nx] == 0:
                boxes[nz][ny][nx] = 1
                queue.append((nz, ny, nx, days + 1))

    # 모든 토마토가 익었는지 확인
    for h in range(H):
        for n in range(N):
            if 0 in boxes[h][n]:  # 익지 않은 토마토가 남아있다면
                return -1

    return max_days  # 모든 토마토가 익는 데 걸리는 최소 일수


# 사용자 입력 처리
M, N, H = map(int, input().split())  # 상자 가로 크기, 세로 크기, 높이
graph = []

for h in range(H):
    layer = []
    for n in range(N):
        row = list(map(int, input().split()))
        layer.append(row)
    graph.append(layer)

# 함수 호출 및 결과 출력
result = bfs_tomato_ripening(M, N, H, graph)
print(result)