# https://school.programmers.co.kr/learn/courses/30/lessons/43236

def remove_min_rock(rocks):
    min_idx = 0
    # 가장 작은 값의 위치 찾기
    for i in range(1, len(rocks)):
        if rocks[min_idx] > rocks[i]:
            min_idx = i

    # 가장 작은 값의 왼쪽 또는 오른쪽 값과 합치기
    if 0 < min_idx < len(rocks) - 1:    # 중간 요소인 경우
        if rocks[min_idx-1] < rocks[min_idx+1]:
            rocks[min_idx-1] = rocks[min_idx-1] + rocks[min_idx]
        else:
            rocks[min_idx + 1] = rocks[min_idx + 1] + rocks[min_idx]
    elif min_idx == 0:  # 첫번째 요소인 경우
        rocks[min_idx + 1] = rocks[min_idx + 1] + rocks[min_idx]
    elif min_idx == len(rocks)-1:   # 마지막 요소인 경우
        rocks[min_idx - 1] = rocks[min_idx - 1] + rocks[min_idx]
    del rocks[min_idx]


def solution(distance, rocks, n):
    answer = 0
    rocks = [0] + rocks + [distance]
    rocks.sort()
    gaps = []
    for i in range(1, len(rocks)):
        gaps.append(rocks[i] - rocks[i-1])

    for _ in range(n):
        remove_min_rock(gaps)

    return min(gaps)


if __name__ == "__main__":
    print(solution(25, [2, 14, 11, 21, 17]	, 2))   # 4