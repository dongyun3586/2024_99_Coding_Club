# https://school.programmers.co.kr/learn/courses/30/lessons/118667
# 2개의 테스트 케이스에서 시간 초과
from collections import deque

def solution(queue1, queue2):
    answer = -1
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    middle = (sum1 + sum2) // 2

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    count = 0
    while queue1 and queue2:
        if sum1 == middle:
            answer = count
            break
        elif sum1 > middle:
            num = queue1.popleft()
            sum1 -= num
        else:
            num = queue2.popleft()
            sum1 += num
        count += 1
    return answer


if __name__ == "__main__":
    print(solution([3, 2, 7, 2], [4, 6, 5, 1]))     # 2
    print(solution([1, 2, 1, 2],	[1, 10, 1, 2]))     # 7
    print(solution([1, 1], [1, 5]))     # -1