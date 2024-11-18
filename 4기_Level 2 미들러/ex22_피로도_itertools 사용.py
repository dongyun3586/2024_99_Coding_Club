# https://school.programmers.co.kr/learn/courses/30/lessons/87946?language=python3
from itertools import permutations


def solution(k, dungeons):
    max_dungeons = 0

    # 모든 던전 순서를 생성
    for perm in permutations(dungeons, len(dungeons)):
        current_fatigue = k
        dungeon_count = 0

        # 현재 순서대로 던전 탐험 시도
        for dungeon in perm:
            required, cost = dungeon
            if current_fatigue >= required:
                current_fatigue -= cost
                dungeon_count += 1
            else:
                break  # 현재 던전을 탐험할 수 없으면 종료

        # 최대 탐험 수 갱신
        max_dungeons = max(max_dungeons, dungeon_count)

    return max_dungeons


if __name__ == '__main__':
    print(solution(80, [[80, 20], [50, 40], [30, 10]]))     # 3
