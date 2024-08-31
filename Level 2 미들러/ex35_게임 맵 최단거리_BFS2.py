# https://school.programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])  # 맵의 크기 저장

    # BFS를 위한 큐 초기화
    queue = deque([(0, 0, 1)])  # (행, 열, 거리)

    while queue:
        x, y, d = queue.popleft()

        # 목적지에 도착한 경우 이동 거리 반환
        if x == n - 1 and y == m - 1:
            return d

        # 네 방향으로 이동
        for dx, dy in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= dx < n and 0 <= dy < m and maps[dx][dy]:
                maps[dx][dy] = 0
                queue.append((dx, dy, d + 1))

    return -1


if __name__ == '__main__':
    print(solution([[1, 0, 1, 1, 1],
                    [1, 0, 1, 0, 1],
                    [1, 0, 1, 1, 1],
                    [1, 1, 1, 0, 1],
                    [0, 0, 0, 0, 1]]))  # 11

    print(solution([[1, 0, 1, 1, 1],
                    [1, 0, 1, 0, 1],
                    [1, 0, 1, 1, 1],
                    [1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 1]]))  # -1
