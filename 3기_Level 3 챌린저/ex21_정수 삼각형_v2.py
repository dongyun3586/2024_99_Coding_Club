# https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    memo = {}   # 메모이제이션을 위한 딕셔너리

    def dfs(row, col):
        # 삼각형 범위를 벗어난 경우 0 반환
        if row >= len(triangle) or col > row:
            return 0

        # 이미 계산된 경우 메모된 값 반환
        if (row, col) in memo:
            return memo[(row, col)]

        # 현재 위치의 값과 아래 두 경로의 최대 값을 더한 값을 메모
        memo[(row, col)] = triangle[row][col] + max(dfs(row + 1, col), dfs(row + 1, col + 1))

        return memo[(row, col)]

    # 꼭대기에서 시작
    return dfs(0, 0)


if __name__ == '__main__':
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))    # 30