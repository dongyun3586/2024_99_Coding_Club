# https://school.programmers.co.kr/learn/courses/30/lessons/178871
# 시간 초과
def solution(players, callings):
    for called_name in callings:
        for idx, name in enumerate(players):
            if name == called_name:
                players[idx], players[idx-1] = players[idx-1], players[idx]
    return players


if __name__ == "__main__":
    print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))
    # result: ["mumu", "kai", "mine", "soe", "poe"]