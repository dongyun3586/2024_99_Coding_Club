# https://school.programmers.co.kr/learn/courses/30/lessons/42586
import math

def solution(progresses, speeds):
    answer = []

    # 0번 index의 작업을 시작 작업으로 설정, 시작 작업의 남은 일수 계산
    start_index = 0
    start_days = math.ceil((100 - progresses[start_index]) / speeds[start_index])
    count = 1

    # 두 번째 작업부터 마지막 작업까지 반복 처리
    for i in range(1, len(progresses)):  # 1 ~ n-1
        current_days = math.ceil((100 - progresses[i]) / speeds[i]) # 현재 작업의 남은 일수 계산
        if current_days <= start_days:  # 현재 작업의 남은 일수가 시작 작업의 남은 일수 보다 작은 경우 count + 1
            count += 1
        else:   # 현재 작업이 시작 작업보다 늦게 끝나는 경우
            answer.append(count)    # 시작 작업부터 현재 작업 직전 까지의 작업 수 count 기록
            # 현재 작업을 시작 작업으로 초기화
            start_index = i
            start_days = math.ceil((100 - progresses[start_index]) / speeds[start_index])
            count = 1

    # 마지막에 처리되지 않은 작업의 개수 추가
    if start_index < len(progresses):
        answer.append(len(progresses[start_index:]))
    return answer


if __name__ == "__main__":
    print(solution([93, 30, 55], [1, 30, 5]))   # 	[2, 1]
    print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))  # [1, 3, 2]