# https://school.programmers.co.kr/learn/courses/30/lessons/42626

from heapq import heapify, heappush, heappop

def solution(scoville, K):
    heapify(scoville)   # scoville 리스트를 힙으로 변환
    count = 0
    while len(scoville) > 1:
        min1, min2 = heappop(scoville), heappop(scoville)
        if min1 >= K:
            return count

        heappush(scoville, min1 + (min2 * 2))
        count += 1

    return -1 if scoville[0] < K else count


if __name__ == "__main__":
    print(solution([1, 2, 3, 9, 10, 12],7))     # 2