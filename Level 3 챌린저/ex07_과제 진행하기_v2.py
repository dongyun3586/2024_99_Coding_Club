# https://school.programmers.co.kr/learn/courses/30/lessons/176962

def solution(plans):
    # 입력 데이터 파싱: 각 과제의 시작 시간과 진행 시간을 분 단위로 변환하여 계산하기 쉽게 만든다.
    plans = [[job_name, int(start_t[:2]) * 60 + int(start_t[3:]), int(play_t)] for job_name, start_t, play_t in plans]

    # 과제 정렬: 과제 시작 시간 순서대로 오름차순 정렬
    plans = sorted(plans, key=lambda x: x[1])

    answer = []
    stack = []  # 현재 진행 중인 과제와 중단된 과제를 관리하기 위한 스택
    current_task = plans[0]  # # 첫 번째 과제를 현재 과제로 설정

    # 순차적으로 과제 처리
    for i in range(1, len(plans)):
        next_task = plans[i]
        current_end_time = current_task[1] + current_task[2]

        if current_end_time <= next_task[1]:  # 현재 과제가 끝나는 시간이 다음 과제 시작 시간보다 빠르거나 같으면(일찍 끝나면)
            answer.append(current_task[0])
            time_gap = next_task[1] - current_end_time

            # time_gap이 남았다면 스택에 있는 과제들을 처리
            while stack and time_gap > 0:
                paused_task = stack.pop()
                if paused_task[2] <= time_gap:
                    answer(paused_task[0])
                    time_gap -= paused_task[2]
                else:
                    paused_task[2] -= time_gap
                    stack.append(paused_task)
                    break
        else:  # 현재 과제가 끝나기 전에 새로운 과제를 시작해야 하는 경우
            current_task[2] -= next_task[1] - current_task[1]
            stack.append(current_task)

        current_task = next_task

    # 마지막 과제 처리
    answer.append(current_task[0])

    # 스택에 남아 있는 과제 처리
    while stack:
        answer.append(stack.pop()[0])
    return answer


if __name__ == "__main__":
    print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"],
                    ["math", "12:30", "40"]]))  # ["korean", "english", "math"]
    print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"],
                    ["computer", "12:30", "100"]]))  # ["science", "history", "computer", "music"]
    print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))  # ["bbb", "ccc", "aaa"]
