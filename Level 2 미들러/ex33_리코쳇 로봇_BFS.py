# https://school.programmers.co.kr/learn/courses/30/lessons/169199
from collections import deque


def solution(board):
    n, m = len(board), len(board[0])  # board의 행, 열 개수

    # 각각 로봇의 시작 위치와 목표 지점의 위치를 저장할 변수
    start, goal = None, None

    # 보드의 모든 칸을 탐색하면서 시작지점(R)과 목표지점(G)의 위치 찾기
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = (i, j)
            elif board[i][j] == 'G':
                goal = (i, j)

    # BFS 초기화
    queue = deque([(start[0], start[1], 0)])  # (x, y, 이동 횟수 0)
    visited = set()     # 이미 방문한 위치를 기록하는 집합(set)으로, 중복 방문을 방지
    visited.add(start)

    # 방향 벡터 설정: 로봇이 이동할 수 있는 네 방향(상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y, moves = queue.popleft()

        # 목표 지점에 도달한 경우
        if (x, y) == goal:
            return moves

        # 4 방향 탐색(상, 하, 좌, 우)
        for dx, dy in directions:
            new_x, new_y = x, y  # 현재 위치에서 새로운 위치로 이동할 때 사용할 변수

            # 로봇이 보드의 경계 안에 있고 장애물('D')에 부딪히지 않는 한, 해당 방향으로 계속 이동
            while 0 <= new_x + dx < n and 0 <= new_y + dy < m and board[new_x + dx][new_y + dy] != 'D':
                new_x += dx
                new_y += dy

            # 새로 도착한 위치가 이전에 방문한 적이 없다면 해당 위치를 방문처리하고 큐에 추가(이동횟수 1 증가시킴)
            if (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append((new_x, new_y, moves + 1))

    return -1    # 목표 지점에 도달할 수 없는 경우


if __name__ == '__main__':
    print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))  # 7
    print(solution([".D.R", "....", ".G..", "...D"]))  # -1
