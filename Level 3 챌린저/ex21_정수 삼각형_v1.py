# https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    # 삼각형의 밑에서부터 거꾸로 올라가며 최대 합을 계산
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            # 현재 위치에서 선택 가능한 아래 두 개의 값 중 큰 값을 선택
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    # 최종적으로 triangle[0][0]에는 최대 합이 저장되어 있음
    return triangle[0][0]


if __name__ == '__main__':
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))    # 30