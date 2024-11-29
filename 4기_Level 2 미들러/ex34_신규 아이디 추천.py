# https://school.programmers.co.kr/learn/courses/30/lessons/72410

import re


def solution(new_id):
    # 1단계: 모든 대문자를 소문자로 변환
    new_id = new_id.lower()

    # 2단계: 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자 제거
    new_id = re.sub(r"[^a-z0-9-_.]", "", new_id)

    # 3단계: 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    new_id = re.sub(r"\.{2,}", ".", new_id)

    # 4단계: 마침표(.)가 처음이나 끝에 위치하면 제거
    new_id = new_id.strip(".")

    # 5단계: 빈 문자열이라면 "a"를 대입
    if new_id == "":
        new_id = "a"

    # 6단계: 길이가 16자 이상이면 첫 15개의 문자를 제외한 나머지를 제거
    #        제거 후 마침표가 끝에 위치하면 제거
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.rstrip(".")

    # 7단계: 길이가 2자 이하라면, 길이가 3이 될 때까지 마지막 문자를 반복해서 붙임
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id

if __name__ == "__main__":
    # Test cases
    print(solution("...!@BaT#*..y.abcdefghijklm"))  # "bat.y.abcdefghi"
    print(solution("z-+.^."))  # "z--"
    print(solution("=.="))  # "aaa"
    print(solution("123_.def"))  # "123_.def"
    print(solution("abcdefghijklmn.p"))  # "abcdefghijklmn"