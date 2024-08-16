# https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players, callings):
    # 선수의 이름을 key로 하고, 위치(index)를 값으로 하는 딕셔너리 생성
    player_pos = {player: idx for idx, player in enumerate(players)}

    # callings 배열 처리
    for name in callings:
        current_pos = player_pos[name]  # 해설진이 부른 선수의 이름으로 선수의 배열 index 찾기

        # 해당 선수와 앞 선수의 위치를 교환
        if current_pos > 0:  # 현재 1등이 아닌 경우에만
            prev_player = players[current_pos - 1]  # 앞 선수의 이름

            # 배열에서 두 선수의 위치를 교환(이름 교환)
            players[current_pos], players[current_pos - 1] = players[current_pos - 1], players[current_pos]

            # 딕셔너리에서 두 선수의 배열 index 업데이트
            player_pos[name] -= 1
            player_pos[prev_player] += 1

    return players


if __name__ == "__main__":
    print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))
    # result: ["mumu", "kai", "mine", "soe", "poe"]
