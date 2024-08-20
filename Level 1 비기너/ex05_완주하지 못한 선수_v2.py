# https://school.programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p

    return participant[-1]


if __name__ == '__main__':
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))  # "leo"
    print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],
                   ["josipa", "filipa", "marina", "nikola"]))  # "vinko"
    print(solution(["mislav", "stanko", "mislav", "ana"],
                   ["stanko", "ana", "mislav"]))  # "mislav"
