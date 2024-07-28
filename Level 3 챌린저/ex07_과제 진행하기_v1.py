# https://school.programmers.co.kr/learn/courses/30/lessons/176962

def solution(plans):
    # 입력 데이터 파싱: 각 과제의 시작 시간과 진행 시간을 분 단위로 변환하여 계산하기 쉽게 만든다.
    plans = [[job_name, int(start_t[:2])*60+int(start_t[3:]), int(play_t)] for job_name, start_t, play_t in plans]

    # 과제 정렬: 과제 시작 시간 순서대로 오름차순 정렬
    plans = sorted(plans, key=lambda x: x[1])

    answer = []
    stack = []  # 현재 진행 중인 과제와 중단된 과제를 관리하기 위한 스택
    current_task = plans[0]

    # 순차적으로 과제 처리
    for next_task in plans[1:]:
        current_task[2] -= next_task[1] - current_task[1]
        if current_task[2] == 0:
            answer.append(current_task[0])
        elif current_task[2] < 0:
            answer.append(current_task[0])
            t = -current_task[2]    # 남는 시간
            while stack and t:
                j = stack.pop()
                if j[2] - t < 0:
                    answer.append(j[0])
                    t -= j[2]
                else:
                    j[2] -= t
                    stack.append(j)
                    break
        else:
            stack.append(current_task)
        current_task = next_task

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
