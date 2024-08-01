# https://school.programmers.co.kr/learn/courses/30/lessons/42628
from heapq import heappush, heappop

def solution(operations):
    min_heap = []
    max_heap = []
    length = 0

    for i in operations:
        o, v = i.split()
        if o == 'D' and length:
            v = int(v)
            if v > 0:   # 최댓값 삭제
                heappop(max_heap)
            else:       # 최솟값 삭제
                heappop(min_heap)
            length -= 1
        elif o == 'I':
            heappush(min_heap, int(v))
            heappush(max_heap, -int(v))
            length += 1
    return [-heappop(max_heap), heappop(min_heap)] if length else [0, 0]


if __name__ == "__main__":
    print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])) # [0,0]
    print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))    # [333, -45]
    print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]))