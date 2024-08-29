# https://school.programmers.co.kr/learn/courses/30/lessons/172927
'''
이 접근 방식은 항상 최적의 해를 보장하지 않는다.
특정 테스트 케이스에서는 모든 그룹을 최적화된 방식으로 채굴하지 못할 수 있다.
'''
def solution(picks, minerals):
    # 곡괭이별 피로도
    fatigue = {
        'diamond': [1, 5, 25],
        'iron': [1, 1, 5],
        'stone': [1, 1, 1]
    }

    # 5개씩 광물을 그룹화
    mineral_groups = [minerals[i:i + 5] for i in range(0, len(minerals), 5)]

    # 각 그룹별로 (다이아몬드, 철, 돌) 곡괭이를 사용했을 때 피로도 모두 계산
    group_fatigue = []
    for group in mineral_groups:
        dia_fatigue = sum(fatigue[m][0] for m in group)
        iron_fatigue = sum(fatigue[m][1] for m in group)
        stone_fatigue = sum(fatigue[m][2] for m in group)
        group_fatigue.append((dia_fatigue, iron_fatigue, stone_fatigue))

    # 피로도가 큰 순서대로 그룹 정렬
    group_fatigue.sort(key=lambda x: (x[2], x[1], x[0]), reverse=True)

    total_fatigue = 0
    for dia_fatigue, iron_fatigue, stone_fatigue in group_fatigue:
        if picks[0] > 0:  # 다이아몬드 곡괭이 사용
            total_fatigue += dia_fatigue
            picks[0] -= 1
        elif picks[1] > 0:  # 철 곡괭이 사용
            total_fatigue += iron_fatigue
            picks[1] -= 1
        elif picks[2] > 0:  # 돌 곡괭이 사용
            total_fatigue += stone_fatigue
            picks[2] -= 1
        else:
            break  # 사용할 곡괭이가 없으면 종료

    return total_fatigue


if __name__ == '__main__':
    print(solution([1, 3, 2],
                   ["diamond", "diamond", "diamond", "iron", "iron",
                    "diamond", "iron", "stone"]))  # 12
    print(solution([0, 1, 1],
                   ["diamond", "diamond", "diamond", "diamond", "diamond",
                    "iron", "iron", "iron", "iron", "iron",
                    "diamond"]))  # 50
    print(solution([1, 0, 1],
                   ["stone", "stone", "stone", "stone", "stone",
                    "iron", "iron", "iron", "iron", "iron",
                    "diamond", "diamond"]))     # 10
