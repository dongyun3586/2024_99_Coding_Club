# https://school.programmers.co.kr/learn/courses/30/lessons/147355
def solution(t, p):
    len_p = len(p)  # p의 길이
    p_num = int(p)  # p를 정수로 변환
    count = 0  # 조건을 만족하는 부분 문자열 개수

    # t에서 길이가 len_p인 부분 문자열을 순차적으로 확인
    for i in range(len(t) - len_p + 1):
        substring = t[i:i + len_p]  # 길이가 len_p인 부분 문자열
        if int(substring) <= p_num:  # 부분 문자열을 정수로 변환 후 비교
            count += 1

    return count


if __name__ == '__main__':
    print(solution("3141592", "271"))  # 2
    print(solution("500220839878", "7"))  # 8
    print(solution("10203", "15"))  # 3
