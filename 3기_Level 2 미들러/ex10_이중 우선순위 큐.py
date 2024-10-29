# https://school.programmers.co.kr/learn/courses/30/lessons/42628

from heapq import heappush, heappop
from collections import defaultdict

def solution(operations):
    min_heap = []
    max_heap = []
    value_dict = defaultdict(int)

    for operation in operations:
        if operation.startswith('I'):
            _, num = operation.split()
            num = int(num)
            heappush(min_heap, num)
            heappush(max_heap, -num)
            value_dict[num] += 1
        elif operation == 'D 1':
            while max_heap:
                num = -heappop(max_heap)
                if value_dict[num] > 0: # 존재하는 값이 아니면 제거
                    value_dict[num] -= 1
                    break
        else:
            while min_heap:
                num = heappop(min_heap)
                if value_dict[num] > 0:  # 존재하는 값이 아니면 제거
                    value_dict[num] -= 1
                    break


    while max_heap and value_dict[-max_heap[0]] == 0:
        heappop(max_heap)
    while min_heap and value_dict[min_heap[0]] == 0:
        heappop(min_heap)

    return [-heappop(max_heap), heappop(min_heap)] if max_heap and min_heap else [0, 0]

if __name__ == "__main__":
    print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))     # 	[0,0]
    print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	))      # [333, -45]
    print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]))       # [6, 5]