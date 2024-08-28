# https://school.programmers.co.kr/learn/courses/30/lessons/142085
import heapq


def solution(n, k, enemy):
    max_heap = []               # 무적권으로 막은 라운드를 저장하기 위한 최대힙(최대힙을 구현을 위해 음수로 저장)
    total_soldiers_used = 0     # 현재까지 사용된 총 병사 수 추적 변수

    # 라운드별 처리: 각 라운드의 적 수를 반복적으로 확인
    for i in range(len(enemy)):
        # 병사로 적을 막을 수 있는 경우: 병사 소모
        if total_soldiers_used + enemy[i] <= n:
            total_soldiers_used += enemy[i]     # 병사를 소모하여 적을 막고, 소모된 병사 수를 total_soldiers_used에 추가
            heapq.heappush(max_heap, -enemy[i])  # 현재 라운드의 적 수를 최대 힙에 음수로 저장
        elif k > 0:     # 병사로 현재 라운드의 적을 막을 수 없는데 무적권이 남은 경우
            # 현재 라운드의 적이 이전에 막았던 라운드의 적 수보다 적은 경우
            if max_heap and -max_heap[0] > enemy[i]:
                # 가장 많은 적이 등장했던 라운드를 무적권으로 막고, 현재 라운드를 병사로 막음
                # 사용된 병수 수에서 이전에 막았던 가장 많은 적의 수를 빼고, 현재 라운드의 적 수를 추가함.
                total_soldiers_used += heapq.heappop(max_heap) + enemy[i]
                heapq.heappush(max_heap, -enemy[i])  # 현재 라운드의 적 수를 최대 힙에 음수로 저장
            k -= 1  # 무적권 차감
        else:
            return i    # 병사도 부족하고 무적권도 없는 경우, 현재 라운드 번호 i를 반환하며 게임 종료

    # 모든 라운드를 반복하고 나서도 병사나 무적권이 남아 모든 라운드를 방어할 수 있는 경우 전체 라운드 수 반환
    return len(enemy)


if __name__ == '__main__':
    print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))    # 5
    print(solution(2, 4, 	[3, 3, 3, 3]))  # 4
