def solution(n):
    answer = 0
    columns = [-1] * n  # 각 행의 퀸 위치를 저장하는 1차원 리스트

    def is_safe(row, col):
        # 이전 행에 배치된 퀸과 같은 열 또는 대각선에 있는지 확인
        for prev_row in range(row):
            prev_col = columns[prev_row]
            if prev_col == col or abs(prev_row - row) == abs(prev_col - col):
                return False
        return True

    def dfs(row):
        nonlocal answer
        # 모든 퀸이 성공적으로 배치된 경우
        if row == n:
            answer += 1
            return

        for col in range(n):
            if is_safe(row, col):  # 현재 위치가 안전한 경우
                columns[row] = col  # 퀸 배치
                dfs(row + 1)        # 다음 행 탐색
                columns[row] = -1   # 백트래킹: 퀸 배치를 제거

    dfs(0)  # 첫 번째 행부터 탐색 시작
    return answer


if __name__ == "__main__":
    print(solution(4))  # 2
    print(solution(8))  # 92
