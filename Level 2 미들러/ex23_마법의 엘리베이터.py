# https://school.programmers.co.kr/learn/courses/30/lessons/148653

def solution(storey):
    count = 0

    while storey > 0:               # storey를 0으로 만들 때까지 반복
        remainder = storey % 10     # 현재 1의 자리의 값 계산

        # 각 자리수에서 버튼을 누르는 횟수를 최소화하기 위해 조건문을 사용
        if remainder > 5:       # 현재 자리의 숫자가 5보다 큰 경우(6, 7, 8, 9): 층을 올라감.
            count += (10 - remainder)
            storey += 10 - remainder
        elif remainder == 5:    # 현재 자리의 숫자가 5인 경우: 다음 자리(즉, 상위 자리)의 숫자를 고려한다.
            if (storey // 10) % 10 >= 5:    # 만약 다음 자리의 숫자가 5 이상이라면 올림
                count += (10 - remainder)
                storey += 10 - remainder
            else:                           # 만약 다음 자리의 숫자가 5 미만 이라면 뺀다.
                count += remainder
                storey -= remainder
        else:                               # 현재 자리의 숫자가 5보다 작은 경우(1, 2, 3, 4) 그 숫자만큼 뺀다.
            count += remainder
            storey -= remainder

        storey //= 10    # 상위 자리로 이동

    return count


if __name__ == '__main__':
    print(solution(16))     # 6
    print(solution(2554))   # 16