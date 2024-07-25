# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def compress_string(s, unit):
    compressed = ""
    prev = s[:unit]     # 첫 번째 부분 문자열
    count = 1

    # 문자열 단위별로 반복: 문자열이 반복되면 count += 1, 반복되지 않는 경우 그대로 추가
    for i in range(unit, len(s), unit):
        if s[i:i + unit] == prev:   # 단위별로 현재 문자열이 이전 문자열과 같으면 count + 1
            count += 1
        else:   # 현재 문자열이 이전 문자열과 다르면
            if count > 1:   # 현재까지 반복된 문자열이 있으면
                compressed += str(count) + prev  # 반복 횟수 + 반복된 이전 문자열
            else:           # 반복된 문자열이 없으면
                compressed += prev  # 이전 문자열 그대로 추가
            prev = s[i:i + unit]    # 현재 위치로 이전 문자열 갱신
            count = 1               # count 변수값 1로 초기화

    # 마지막 부분 문자열 처리
    if count > 1:
        compressed += str(count) + prev
    else:
        compressed += prev

    return compressed   # 압축된 문자열 반환


def solution(s):
    if len(s) == 1:
        return 1

    min_length = len(s)     # 압축된 문자열의 최소 길이 저장 변수

    # 문자열을 1개 단위부터 최대 문자열 길이의 절반까지의 단위로 잘라본다.
    for unit in range(1, len(s) // 2 + 1):
        compressed = compress_string(s, unit)           # 압축된 문자열의 길이 계산
        min_length = min(min_length, len(compressed))   # 압축된 문자열 길이 중 가장 짧은 길이

    return min_length


if __name__ == '__main__':
    print(solution('aabbaccc'))                 # 7
    print(solution('ababcdcdababcdcd'))         # 9
    print(solution('abcabcdede'))               # 8
    print(solution('abcabcabcabcdededededede')) # 14
    print(solution('xababcdcdababcdcd'))        # 17
