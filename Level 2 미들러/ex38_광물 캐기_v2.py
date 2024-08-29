def solution(picks, minerals):
    # 각 곡괭이로 광물을 캘 때 소모되는 피로도
    fatigue = {
        'diamond': [1, 5, 25],
        'iron': [1, 1, 5],
        'stone': [1, 1, 1]
    }

    # 광물 그룹화: minerals 리스트를 5개씩 나누어 mineral_groups 리스트로 생성
    mineral_groups = [minerals[i:i + 5] for i in range(0, len(minerals), 5)]

    # 각 그룹별 피로도 계산: (다이아몬드, 철, 돌)
    group_fatigue = []
    for group in mineral_groups:
        dia_fatigue = sum(fatigue[m][0] for m in group)     # 다이아몬드 곡괭이를 사용했을 때의 총 피로도
        iron_fatigue = sum(fatigue[m][1] for m in group)    # 철 곡괭이를 사용했을 때의 총 피로도
        stone_fatigue = sum(fatigue[m][2] for m in group)   # 돌 곡괭이를 사용했을 때의 총 피로도
        group_fatigue.append((dia_fatigue, iron_fatigue, stone_fatigue))    # 계산된 피로도는 리스트에 튜플 형태로 저장

    # 백트래킹으로 모든 경우의 수 탐색
    def dfs(index, remaining_picks, current_fatigue):
        '''
        백트래킹을 통해 모든 경우의 수를 탐색하여 최소 피로도를 찾는다.
        :param index: 현재 처리 중인 그룹의 인덱스
        :param remaining_picks: 사용 가능한 곡괭이 수 [dia, iron, stone] 순
        :param current_fatigue: 현재까지 계산된 누적 피로도
        :return:
        '''
        # 종료 조건: 모든 그룹을 처리했거나, 사용할 곡괭이가 더 이상 없는 경우
        if index == len(group_fatigue) or all(pick == 0 for pick in remaining_picks):
            return current_fatigue      # 현재까지의 누적 피로도

        min_fatigue = float('inf')

        # 각 곡괭이를 사용해 보면서 최소 피로도 계산
        for i in range(3):
            if remaining_picks[i] > 0:
                new_remaining_picks = remaining_picks[:]
                new_remaining_picks[i] -= 1
                next_fatigue = current_fatigue + group_fatigue[index][i]
                min_fatigue = min(min_fatigue, dfs(index + 1, new_remaining_picks, next_fatigue))

        return min_fatigue

    return dfs(0, picks, 0)


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
                    "diamond", "diamond"]))  # 10
