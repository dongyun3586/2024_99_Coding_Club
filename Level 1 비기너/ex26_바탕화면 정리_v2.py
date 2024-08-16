# https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    # 초기값 설정
    lux, luy = float('inf'), float('inf')
    rdx, rdy = -float('inf'), -float('inf')

    # 바탕화면의 모든 칸을 확인하며 파일 위치 파악
    for r in range(len(wallpaper)):
        for c in range(len(wallpaper[0])):
            if wallpaper[r][c] == '#':
                # 가장 위쪽과 가장 왼쪽 좌표 찾기
                lux = min(lux, r)
                luy = min(luy, c)
                # 가장 아래쪽과 가장 오른쪽 좌표 찾기
                rdx = max(rdx, r + 1)
                rdy = max(rdy, c + 1)

    # 드래그의 시작점과 끝점 반환
    return [lux, luy, rdx, rdy]


# 테스트 실행
print(solution([".#...", "..#..", "...#."]))  # [0, 1, 3, 4]
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))  # [1, 3, 5, 8]
print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))  # [0, 0, 7, 9]
print(solution(["..", "#."]))  # [1, 0, 2, 1]

