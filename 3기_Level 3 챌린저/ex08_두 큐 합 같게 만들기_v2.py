# https://school.programmers.co.kr/learn/courses/30/lessons/118667
# 경계 조건을 이용하여 해결할 수 없는 경우 -1 리턴
from collections import deque


def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    s1 = sum(queue1)
    s2 = sum(queue2)

    if (s1 + s2) % 2:
        return -1

    limit = len(queue1) * 3 - 3

    cnt = 0
    while cnt <= limit:
        if s1 < s2:
            cur = queue2.popleft()
            queue1.append(cur)
            s1 += cur
            s2 -= cur
        elif s2 < s1:
            cur = queue1.popleft()
            queue2.append(cur)
            s2 += cur
            s1 -= cur
        else:
            return cnt
        cnt += 1

    return -1


if __name__ == "__main__":
    print(solution([3, 2, 7, 2], [4, 6, 5, 1]))  # 2
    print(solution([1, 2, 1, 2], [1, 10, 1, 2]))  # 7
    print(solution([1, 1], [1, 5]))  # -1
