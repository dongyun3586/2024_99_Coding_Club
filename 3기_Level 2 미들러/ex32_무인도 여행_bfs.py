# https://school.programmers.co.kr/learn/courses/30/lessons/154540
from collections import deque


def solution(maps):
    def bfs(i, j):
        queue = deque([(i, j)])
        count = maps[i][j]
        maps[i][j] = 0

        while queue:
            x, y = queue.popleft()
            for dx, dy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= dx < r and 0 <= dy < c and maps[dx][dy] > 0:
                    count += maps[dx][dy]
                    maps[dx][dy] = 0
                    queue.append((dx, dy))

        return count

    # 맵을 숫자로 변환
    maps = [[0 if c == 'X' else int(c) for c in s] for s in maps]
    r, c = len(maps), len(maps[0])

    answer = []
    for i in range(r):
        for j in range(c):
            if maps[i][j] != 0:
                answer.append(bfs(i, j))

    return sorted(answer) if answer else [-1]


if __name__ == '__main__':
    print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))  # [1, 1, 27]
    print(solution(["XXX", "XXX", "XXX"]))  # [-1]
