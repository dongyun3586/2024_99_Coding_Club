# https://school.programmers.co.kr/learn/courses/30/lessons/43236
"""주어진 거리와 바위 배열에서 특정 개수의 바위를 제거하여,
각 구간 거리의 최솟값을 최대화하는 문제를 해결하기 위해 이진 탐색을 사용"""
def solution(distance, rocks, n):
    # 바위 위치 정렬
    rocks.sort()

    # 시작점과 끝점 사이의 거리 설정
    left, right = 0, distance
    answer = 0  # 거리의 최솟값 중 가장 큰 값 저장

    # 이진 탐색을 통해 mid 값을 계속 조정하여 최적의 해를 찾는다.
    while left <= right:
        mid = (left + right) // 2  # 구간 거리의 중간값
        current = 0         # 현재 위치를 추적하는 변수, 시작점은 0
        removed_rocks = 0   # 제거한 바위의 수

        # 각 바위를 순회하면서 현재 설정된 mid값보다 작은 거리가 생기면 바위를 제거
        for rock in rocks:
            # 현재 위치(current)에서 시작하여, 각 바위 간의 거리가 mid보다 작으면 해당 바위를 제거
            if rock - current < mid:
                removed_rocks += 1
            else:
                # 현재 위치를 그 바위 위치로 갱신
                current = rock

            # 필요한 만큼 바위를 제거한 경우 탐색 종료
            if removed_rocks > n:
                break

        # 마지막 바위에서 도착점까지의 거리 확인: 이 거리가 mid보다 작다면, 도착점에 도달할 수 없는 것이므로 바위를 추가로 제거
        if distance - current < mid:
            removed_rocks += 1

        # 만약 제거한 바위 수가 n보다 작거나 같으면, mid 거리로 충분히 모든 조건을 만족할 수 있다.
        if removed_rocks <= n:
            # mid값이 가능한 경우, 더 큰 거리 시도
            answer = mid
            left = mid + 1
        else:
            # mid값이 불가능한 경우, 더 작은 거리 시도
            right = mid - 1

    # 이진 탐색이 완료되면, answer에는 가능한 거리의 최솟값 중 가장 큰 값이 저장되어 있다.
    return answer


if __name__ == "__main__":
    print(solution(25, [2, 14, 11, 21, 17]	, 2))   # 4