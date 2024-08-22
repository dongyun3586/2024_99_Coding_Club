# https://school.programmers.co.kr/learn/courses/30/lessons/154540
import sys
sys.setrecursionlimit(10000)     # 재귀 호출 한계를 3000으로 설정


def solution(maps):
    def dfs(r, c):
        nonlocal count
        rows, cols = len(maps), len(maps[0])
        count += maps[r][c]
        maps[r][c] = 0

        for dx, dy in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= dx < rows and 0 <= dy < cols and maps[dx][dy] != 0:
                dfs(dx, dy)


    # 맵을 숫자로 변환
    maps = [[0 if c == 'X' else int(c) for c in s] for s in maps]
    r, c = len(maps), len(maps[0])

    answer = []
    for i in range(r):
        for j in range(c):
            count = 0
            if maps[i][j] != 0:
                dfs(i, j)
                answer.append(count)

    return sorted(answer) if answer else [-1]


if __name__ == '__main__':
    print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))  # [1, 1, 27]
    print(solution(["XXX", "XXX", "XXX"]))  # [-1]
