# https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    answer = [100, 100, -1, -1]
    for r, line in enumerate(wallpaper):
        for c, f in enumerate(line):
            if f == '#':
                if answer[0] > r:
                    answer[0] = r
                if answer[1] > c:
                    answer[1] = c
                if answer[2] <= r:
                    answer[2] = r + 1
                if answer[3] <= c:
                    answer[3] = c + 1
    return answer


if __name__ == '__main__':
    print(solution([".#...", "..#..", "...#."]))  # [0, 1, 3, 4]
    print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))  # [1, 3, 5, 8]
    print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))  # [0, 0, 7, 9]
    print(solution(["..", "#."]))  # [1, 0, 2, 1]
