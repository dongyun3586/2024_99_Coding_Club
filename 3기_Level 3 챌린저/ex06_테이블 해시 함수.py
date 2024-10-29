# https://school.programmers.co.kr/learn/courses/30/lessons/147354

def solution(data, col, row_begin, row_end):
    answer = 0
    # 테이블의 튜플을 col번째 컬럼의 값을 기준으로 오름차순 정렬을 하되, 만약 그 값이 동일하면 기본키인 첫 번째 컬럼의 값을 기준으로 내림차순 정렬
    data = sorted(data, key=lambda x: (x[col-1], -x[0]))

    # 정렬된 데이터에서 S_i를 i 번째 행의 튜플에 대해 각 컬럼의 값을 i 로 나눈 나머지들의 합으로 정의
    # row_begin ≤ i ≤ row_end 인 모든 S_i를 누적하여 bitwise XOR 한 값을 해시 값으로 반환
    for i in range(row_begin-1, row_end):
        # value = 0
        # for j in data[i]:
        #     value += j % (i+1)
        # answer ^= value
        answer ^= sum([j % (i+1) for j in data[i]])
    return answer


if __name__ == "__main__":
    # print(0 ^ 4)    # XOR 계산
    print(solution([[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]], 2, 2, 3))     # 4
