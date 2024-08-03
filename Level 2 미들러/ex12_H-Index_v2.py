# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort(reverse=True)
    for i, citation in enumerate(citations):
        if i >= citation:
            return i
    return len(citations)


if __name__ == "__main__":
    print(solution([3, 0, 6, 1, 5]))        # 3
    print(solution([0]))  # 0
    print(solution([0, 0, 0, 0, 0]))        # 0
    print(solution([1, 11, 111, 1111]))     # 3
    print(solution([1, 2, 3, 5, 6, 7, 10, 11]))     # 5
    print(solution([1, 1, 2, 2, 3, 4, 5, 6, 7]))    # 4
    print(solution([3, 5, 11, 6, 1, 5, 3, 3, 1, 41]))   # 5