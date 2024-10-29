# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort(reverse=True)    # 가장 많이 인용된 논문부터 차례로 비교할 수 있도록 준비
    answer = 0
    for i in range(len(citations)):
        # 논문의 인용 횟수가 i + 1보다 크거나 같은지를 확인
        if i < citations[i]:    # 현재 논문이 i+1번 이상 인용되었는가?
            answer += 1         # 조건을 만족하면 h값 증가
    return answer


if __name__ == "__main__":
    print(solution([3, 0, 6, 1, 5]))        # 3
    print(solution([0]))  # 0
    print(solution([0, 0, 0, 0, 0]))        # 0
    print(solution([1, 11, 111, 1111]))     # 3
    print(solution([1, 2, 3, 5, 6, 7, 10, 11]))     # 5
    print(solution([1, 1, 2, 2, 3, 4, 5, 6, 7]))    # 4
    print(solution([3, 5, 11, 6, 1, 5, 3, 3, 1, 41]))   # 5