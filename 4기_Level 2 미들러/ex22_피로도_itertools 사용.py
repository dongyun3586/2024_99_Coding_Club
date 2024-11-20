# https://school.programmers.co.kr/learn/courses/30/lessons/87946?language=python3
from itertools import permutations


def solution(k, dungeons):  # 유저의 현재 피로도, 던전의 피로도 리스트
    max_count = 0           # 최대 탐험 개수 저장 변수

    # 모든 던전 순서를 생성
    for perm in permutations(dungeons, len(dungeons)):
        current_hp = k
        current_count = 0

        # 현재 던전 순서대로 탐험 시도
        for dungeon in perm:
            required_hp, used_hp = dungeon    # [입장 hp, 소모 hp]
            if current_hp >= required_hp:
                current_hp -= used_hp
                current_count += 1
            else:
                break  # 현재 던전을 탐험할 수 없으면 종료

        # 최대 탐험 수 갱신
        max_count = max(max_count, current_count)

    return max_count


if __name__ == '__main__':
    print(solution(80, [[80, 20], [50, 40], [30, 10]]))     # 3
