# https://school.programmers.co.kr/learn/courses/30/lessons/42586
import math


def solution(progresses, speeds):
    answer = []
    days_left = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]  # 각 작업의 남은 일수를 계산
    start_days = days_left[0]   # 0번 작업의 남은 일수
    count = 1

    for days in days_left[1:]:
        if days <= start_days:  # 현재 작업의 일수가 시작 작업보다 작은 경우: 시작 작업과 같이 종료되기 때문에 count + 1
            count += 1
        else:   # 현재 작업이 시작 작업보다 늦게 끝나는 경우: 시직 작업부터 이전 작업까지의 수 정답에 추가
            answer.append(count)
            start_days = days
            count = 1

    answer.append(count)  # 마지막 남은 작업 개수 추가
    return answer


if __name__ == "__main__":
    print(solution([93, 30, 55], [1, 30, 5]))  # [2, 1]
    print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))  # [1, 3, 2]