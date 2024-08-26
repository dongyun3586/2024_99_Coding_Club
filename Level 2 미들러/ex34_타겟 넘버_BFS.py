# https://school.programmers.co.kr/learn/courses/30/lessons/43165
from collections import deque


def solution(numbers, target):
    queue = deque([(0, 0)])     # 초기 큐 설정: (현재 합계, 현재 인덱스)
    answer = 0  # 목표 숫자를 만들 수 있는 경우의 수를 저장하는 변수

    while queue:
        current_sum, index = queue.popleft()

        # 모든 숫자를 사용한 경우
        if index == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            # 현재 인덱스에 있는 숫자를 더하는 경우
            queue.append((current_sum + numbers[index], index + 1))
            # 현재 인덱스에 있는 숫자를 빼는 경우
            queue.append((current_sum - numbers[index], index + 1))

    return answer


if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3))  # 5
    print(solution([4, 1, 2, 1], 4))  # 2
