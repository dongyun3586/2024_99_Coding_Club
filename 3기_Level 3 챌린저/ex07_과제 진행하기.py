# https://school.programmers.co.kr/learn/courses/30/lessons/176962

def solution(plans):
    # 입력 데이터 파싱: 각 과제의 시작 시간과 진행 시간을 분 단위로 변환하여 계산하기 쉽게 만든다.
    plans = [[job_name, int(start_t[:2])*60+int(start_t[3:]), int(play_t)] for job_name, start_t, play_t in plans]

    # 과제 정렬: 과제 시작 시간 순서대로 오름차순 정렬
    plans = sorted(plans, key=lambda x: x[1])

    answer = []
    stack = []  # 현재 진행 중인 과제와 중단된 과제를 관리하기 위한 스택
    current_task = plans[0]     # 첫 번째 과제를 현재 과제로 설정

    # 순차적으로 과제 처리
    for next_task in plans[1:]:
        current_task_endtime = current_task[1] + current_task[2]    # 현재 작업이 끝나는 시간

        if current_task_endtime <= next_task[1]:                    # 현재 작업이 다음 작업 시작시간보다 먼저 끝나는 경우
            answer.append((current_task[0]))                        # 현재 작업 종결 처리
            remaining_time = next_task[1] - current_task_endtime    # 남은 시간: 다음 작업 시작시간 - 현재작업 종료 시간

            while stack:
                paused_task = stack.pop()
                if paused_task[1] - remaining_time <= 0:    # 스택에서 꺼낸 작업이 종료되는 경우
                    answer.append(paused_task[0])
                    remaining_time -= paused_task[1]
                else:                                       # 스택에서 꺼낸 작업이 종료되지 않는 경우
                    paused_task[1] -= remaining_time
                    stack.append(paused_task)
                    break
        else:   # 현재 작업이 끝나지 않은 상태에 새로운 작업이 시작되는 경우
            used_time = next_task[1] - current_task[1]
            stack.append([current_task[0], current_task[2] - used_time])    # 현재 작업의 남은 시간을 감소시킨 후 stack에 삽입

        current_task = next_task    # 현재 작업 교체

    # 마지막 과제 처리
    answer.append(current_task[0])

    # 스택에 남아 있는 과제 처리
    while stack:
        answer.append(stack.pop()[0])
    return answer


if __name__ == "__main__":
    print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))   #  ["korean", "english", "math"]
    print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))   # ["science", "history", "computer", "music"]
    print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))  # ["bbb", "ccc", "aaa"]
    print(solution([["A", "12:00", "50"], ["B", "12:10", "100"], ["C", "13:40", "10"], ["D", "15:00", "30"]]))  #
    print(solution([["A", "00:00", "11"], ["B", "00:10", "10"], ["C", "00:20", "20"], ["D", "00:50", "10"]]))  #
    print(solution([["1", "00:00", "30"], ["2", "00:10", "10"], ["3", "00:30", "10"], ["4", "00:50", "10"]]))
