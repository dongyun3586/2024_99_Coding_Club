# https://school.programmers.co.kr/learn/courses/30/lessons/42576
from collections import defaultdict

def solution(participant, completion):
    D = defaultdict(int)
    # 완주자 리스트를 딕셔너리로 변환
    for name in completion:
        D[name] += 1

    # 모든 참가자 리스트 처리
    for name in participant:
        if name not in D:
            return name
        elif D[name] == 0:
            return name
        else:
            D[name] -= 1
    return None


if __name__ == '__main__':
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))  # "leo"
    print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],
                   ["josipa", "filipa", "marina", "nikola"]))  # "vinko"
    print(solution(["mislav", "stanko", "mislav", "ana"],
                   ["stanko", "ana", "mislav"]))  # "mislav"
