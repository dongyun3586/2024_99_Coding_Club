# https://school.programmers.co.kr/learn/courses/30/lessons/12952

def solution(n):
    board = [[0] * n for _ in range(n)]     # N x N 크기의 체스판을 나타내는 2차원 리스트
    answer = 0                              # 퀸을 서로 공격하지 않게 배치할 수 있는 경우의 수를 저장하는 변수

    def is_safe(row, col):
        # 같은 열에 Queen이 있는지 확인: 현재 row보다 위쪽에 있는 행만 검사
        for prev_row in range(row):
            if board[prev_row][col] == 1:
                return False

        # 왼쪽 또는 오른쪽 대각선에 Queen이 있는지 확인: 왼쪽 위 대각선과 오른쪽 위 대각선을 각각 확인
        for i in range(1, row + 1):
            if col - i >= 0 and board[row - i][col - i] == 1:  # 왼쪽 대각선
                return False
            if col + i < n and board[row - i][col + i] == 1:  # 오른쪽 대각선
                return False
        return True

    # 현재 row에 퀸을 배치할 수 있는 위치를 찾고, 그 위치에 퀸을 배치한 후 다음 행에 대해 재귀적으로 탐색
    def dfs(row):
        nonlocal answer
        # 모든 퀸이 성공적으로 배치되면 True 반환
        if row == n:
            answer += 1
            return

        # 현재 행에서 가능한 모든 열을 시도하며, is_safe 함수를 통해 해당 위치가 안전한지 확인
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 1     # Queen 배치
                dfs(row + 1)            # 다음 행에 대해 재귀호출
                board[row][col] = 0     # 백트래킹: 모든 배치를 찾기 위해 배치된 퀸을 제거하여 다른 가능한 배치를 탐색

    dfs(0)      # 첫 번째 행부터 탐색 시작
    return answer


if __name__ == "__main__":
    print(solution(4))  # 2
    print(solution(8))  # 92
