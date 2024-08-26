# https://www.acmicpc.net/problem/2210
'''
DFS를 사용하여 숫자판에서 가능한 모든 경로를 탐색
각 경로에서 6자리 숫자를 만들어내고, 이를 집합(set)에 추가하여 중복된 숫자를 제거
'''
def dfs(x, y, current_number):
    '''
    x, y는 현재 위치
    current_number는 현재까지 만든 숫자를 나타내는 문자열
    '''
    if len(current_number) == 6:
        unique_numbers.add(current_number)
        return

    # 현재 위치에서 상, 하, 좌, 우 네 방향으로 이
    for dx, dy in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if 0 <= dx < 5 and 0 <= dy < 5:  # 범위 체크
            dfs(dx, dy, current_number + board[dx][dy])

# 입력 받기
board = [input().split() for _ in range(5)]

unique_numbers = set()  # 6자리 숫자를 저장하는 집합

# 숫자판의 각 위치에서 DFS 시작
for i in range(5):
    for j in range(5):
        dfs(i, j, board[i][j])  # board[i][j]는 현재까지의 숫자를 문자열로 저장한 것

# 결과 출력
print(len(unique_numbers))

