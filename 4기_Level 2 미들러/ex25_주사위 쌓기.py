# https://www.acmicpc.net/problem/2116

n = int(input())  # 주사위의 개수
dices = [list(map(int, input().split())) for _ in range(n)]  # 각 주사위의 면 정보를 저장하는 리스트


def max_side_sum(dices):
    other_side_index = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}  # 마주보는 면의 index 정의
    max_sum = 0  # 주사위 옆면 합의 최댓값 저장 변수

    # 첫 주사위의 모든 면을 윗면으로 설정하여 반복
    for top in range(6):
        current_sum = 0     # 현재 주사위 조합에서의 옆면 숫자의 합
        current_top = dices[0][top]  # 현재 주사위의 윗면 값

        # 첫 번째 주사위를 기준으로 순차적으로 다른 주사위를 쌓으면서 옆면의 숫자중 최대값을 누적
        for dice in dices:
            # 아래 주사위의 윗면 숫자가 위에 쌓을 주사위의 아랫면 숫자와 같아야 함.
            bottom_index = dice.index(current_top)  # 위에 쌓을 주사위의 아랫면 index
            top_index = other_side_index[bottom_index]  # 위에 쌓을 주사위의 윗면 index

            # 옆면 최대값 계산 (윗면, 아랫면 제외)
            side_values = [dice[i] for i in range(6) if i not in {top_index, bottom_index}]
            current_sum += max(side_values)

            # 현재 주사위의 윗면 값 갱신
            current_top = dice[top_index]

        # 최댓값 갱신
        max_sum = max(max_sum, current_sum)
    return max_sum


# 결과 출력
print(max_side_sum(dices))
