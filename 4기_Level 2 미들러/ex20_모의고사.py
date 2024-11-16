# https://school.programmers.co.kr/learn/courses/30/lessons/42840?language=python3

def solution(answers):
    result = [1]
    # 각 수포자의 찍기 패턴
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    scores = [0] * 3    # 각 수포자의 정답 수를 저장할 리스트

    # 정답과 비교하며 각 수포자의 점수 계산
    for i in range(len(answers)):
        if p1[i % 5] == answers[i]:
            scores[0] += 1
        if p2[i % 8] == answers[i]:
            scores[1] += 1
        if p3[i % 10] == answers[i]:
            scores[2] += 1

    # 가장 높은 점수를 찾고, 그 점수를 가진 수포자들을 반환
    max_score = max(scores)
    result = [i + 1 for i, score in enumerate(scores) if score == max_score]

    return result


if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5]))  # [1]
    print(solution([1, 3, 2, 4, 2]))  # [1, 2, 3]
