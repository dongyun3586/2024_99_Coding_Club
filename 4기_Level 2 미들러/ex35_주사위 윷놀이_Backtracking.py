#region 게임판
"""
board 딕셔너리는 게임판의 각 위치를 키로, 해당 위치의 정보를 값으로 저장한다.
각 위치의 정보는 또 다른 딕셔너리로, score와 next를 포함한다.
next는 일반적으로 한 개의 요소를 가지지만, 파란색 칸의 경우 두 개의 요소를 가진다.
"""
board = {
    0: {'score': 0, 'next': [1]},
    1: {'score': 2, 'next': [2]},
    2: {'score': 4, 'next': [3]},
    3: {'score': 6, 'next': [4]},
    4: {'score': 8, 'next': [5]},
    5: {'score': 10, 'next': [6, 22]},  # 파란색 칸
    6: {'score': 12, 'next': [7]},
    7: {'score': 14, 'next': [8]},
    8: {'score': 16, 'next': [9]},
    9: {'score': 18, 'next': [10]},
    10: {'score': 20, 'next': [11, 26]},  # 파란색 칸
    11: {'score': 22, 'next': [12]},
    12: {'score': 24, 'next': [13]},
    13: {'score': 26, 'next': [14]},
    14: {'score': 28, 'next': [15]},
    15: {'score': 30, 'next': [16, 28]},  # 파란색 칸
    16: {'score': 32, 'next': [17]},
    17: {'score': 34, 'next': [18]},
    18: {'score': 36, 'next': [19]},
    19: {'score': 38, 'next': [20]},
    20: {'score': 40, 'next': [21]},
    21: {'score': 0, 'next': []},  # 도착 칸: score는 0, next는 빈 리스트
    # 파란색 경로들
    22: {'score': 13, 'next': [23]},
    23: {'score': 16, 'next': [24]},
    24: {'score': 19, 'next': [25]},
    25: {'score': 25, 'next': [31]},
    26: {'score': 22, 'next': [27]},
    27: {'score': 24, 'next': [25]},
    28: {'score': 28, 'next': [29]},
    29: {'score': 27, 'next': [30]},
    30: {'score': 26, 'next': [25]},
    31: {'score': 30, 'next': [32]},
    32: {'score': 35, 'next': [20]},
}
#endregion

# 파란색 칸 목록: 파란색 칸에서 시작할 때는 두 번째 요소인 파란색 경로로 이동한다.
blue_positions = [5, 10, 15]

# 주사위 입력 받기: 사용자로부터 주사위에서 나온 수 10개를
dice = list(map(int, input().split()))

max_score = 0   # 최대 점수 변수


def move(position, steps):  # position: 현재 말의 위치, steps: 이동해야 할 칸 수 (주사위에서 나온 수).
    """말의 이동 함수"""
    if position == 21:  # 도착 칸 이면
        return 21       # 이동할 수 없으므로 그대로 21을 반환
    current = position
    steps_remaining = steps
    first_move = True

    # 이동 조건 체크하면서 한 칸씩 이동
    while steps_remaining > 0:
        # 첫 이동이고, 현재 위치가 파란색 칸이면
        if first_move and current in blue_positions:
            current = board[current]['next'][1]     # 파란색 경로로 이동
        else:
            if not board[current]['next']:          # board[current]['next']가 비어 있다면 도착 칸
                return 21
            current = board[current]['next'][0]     # 빨간색 경로(일반 경로)로 이동
        steps_remaining -= 1
        first_move = False
        if current == 21:   # 만약 current가 도착 칸(21번)이면 반복 종료
            break
    return current   # 이동이 완료된 후의 위치 current를 반환


def dfs(turn, positions, score):
    # turn: 현재 턴 번호 (0부터 시작), positions: 말들의 현재 위치 리스트, score: 현재까지의 총 점수
    global max_score

    # turn이 10이면 (모든 주사위 수를 사용했으면), max_score를 갱신하고 함수를 종료
    if turn == 10:
        if score > max_score:
            max_score = score
        return

    # 말 선택 및 이동
    for i in range(4):  # 4개의 말에 대해 순차적으로 시도(i는 말의 인덱스)
        pos = positions[i]
        if pos == 21:   # 도착 칸에 있는 말은 이동할 수 없으므로 건너뛴다.
            continue

        # move 함수를 사용하여 현재 말의 위치에서 주사위 수만큼 이동한 다음 위치 next_pos를 계산
        next_pos = move(pos, dice[turn])

        # 이동 가능 여부 확인(가지치기): 도착 칸이 아니고, 이동하려는 칸에 다른 말이 있으면 해당 선택을 건너뜀.
        if next_pos != 21 and next_pos in positions:    # 도착 칸인 경우에는 다른 말이 있어도 이동 허용
            continue

        # 말의 위치 업데이트 및 재귀 호출
        original_pos = positions[i]     # 현재 말의 원래 위치를 original_pos에 저장 (백트래킹을 위해)
        positions[i] = next_pos         # 말의 위치 변경

        # dfs 함수를 재귀적으로 호출하여 다음 턴을 진행
        dfs(turn + 1, positions, score + board[next_pos]['score'])

        # 백트래킹: positions[i]를 original_pos로 복원하여 다음 경우를 시도
        positions[i] = original_pos


# 초기 상태로 DFS 시작
dfs(0, [0, 0, 0, 0], 0)
print(max_score)

"""
if next_pos != 21 and next_pos in positions:
    continue 
이동하려는 칸에 다른 말이 있을 때 이동을 불가능하게 하는 조건을 검사하는 코드이다. 
그러나 도착 칸(위치 21번)은 예외적으로 여러 말이 동시에 있을 수 있으므로, 이 경우에는 이동을 허용해야 한다. 
따라서 next_pos != 21 조건을 추가하여 도착 칸인 경우에는 다른 말이 있어도 이동을 허용 한다.
"""