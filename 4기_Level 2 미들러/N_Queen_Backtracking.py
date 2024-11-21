# https://www.acmicpc.net/problem/9663

def is_safe(row, col, queens):
    for r, c in queens:
        # 같은 열에 퀸이 있는지 확인
        if col == c:
            return False
        # 같은 대각선에 퀸이 있는지 확인
        if abs(row - r) == abs(col - c):
            return False
    return True


def solve_n_queens(n, row=0, queens=[]):
    if row == n:  # 모든 퀸을 배치했다면
        return 1  # 한 가지 방법을 찾았으므로 1 반환

    count = 0
    for col in range(n):  # 현재 행의 모든 열에 대해 시도
        if is_safe(row, col, queens):  # 현재 위치에 퀸을 놓아도 되는지 확인
            count += solve_n_queens(n, row + 1, queens + [(row, col)])
    return count


n = int(input())            # n * n 체스판의 크기 n
print(solve_n_queens(n))
