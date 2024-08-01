# https://school.programmers.co.kr/learn/courses/30/lessons/42746
from functools import cmp_to_key


def solution(numbers):
    # 모든 숫자를 문자열로 변환
    numbers = list(map(str, numbers))

    # 정렬 기준을 최대 4자리까지 확장하여 비교
    numbers.sort(key=lambda x: x * 6, reverse=True)

    # 정렬된 결과를 이어붙여 결과 생성
    answer = ''.join(numbers)

    # 예외 처리: 결과가 "0"으로 시작하면 "0" 반환
    return '0' if answer[0] == '0' else answer


if __name__ == "__main__":
    print(solution([6, 10, 2]))             # "6210"
    print(solution([3, 30, 34, 5, 9]))      # "9534330"