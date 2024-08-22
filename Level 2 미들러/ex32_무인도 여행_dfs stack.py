# https://school.programmers.co.kr/learn/courses/30/lessons/154540
def solution(maps):
    def dfs(x, y):
        stack = [(x, y)]
        total_food = 0

        while stack:
            cx, cy = stack.pop()
            if cx < 0 or cy < 0 or cx >= len(maps) or cy >= len(maps[0]) or maps[cx][cy] == 'X':
                continue
            total_food += int(maps[cx][cy])
            maps[cx] = maps[cx][:cy] + 'X' + maps[cx][cy + 1:]  # 방문한 곳을 'X'로 바꾸어 재방문 방지

            # 상하좌우 이동
            stack.append((cx + 1, cy))
            stack.append((cx - 1, cy))
            stack.append((cx, cy + 1))
            stack.append((cx, cy - 1))

        return total_food

    island_foods = []

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != 'X':
                island_foods.append(dfs(i, j))

    return sorted(island_foods) if island_foods else [-1]


if __name__ == '__main__':
    print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))  # [1, 1, 27]
    print(solution(["XXX", "XXX", "XXX"]))  # [-1]
