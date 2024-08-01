# https://school.programmers.co.kr/learn/courses/30/lessons/42746
from functools import cmp_to_key


def solution(numbers):
    numbers = list(map(str, numbers))   # # numbers를 문자열로 변환

    # 두 숫자를 비교하여 어느 쪽을 앞에 놓는 것이 더 큰 수를 만드는지를 결정하는 비교 함수
    def compare(x, y):
        if x + y > y + x:
            return -1   # 첫 번째 인자(x)가 두 번째 인자(y)보다 작으면 음수 반환
        elif x + y < y + x:
            return 1    # 첫 번째 인자(x)가 두 번째 인자(y)보다 크면 양수 반환
        else:
            return 0    # 두 인자가 같으면 0 반환

    # 비교 함수를 사용하여 정렬
    numbers.sort(key=cmp_to_key(compare))   # functools.cmp_to_key를 사용하여 직접 요소를 비교하는 함수를 정의

    # 정렬된 값들을 하나의 문자열로 이어 붙인다.
    answer = ''.join(numbers)

    # 가장 큰 수가 0으로 시작하면, 이는 모든 숫자가 0이라는 뜻
    return '0' if answer[0] == '0' else answer


if __name__ == "__main__":
    print(solution([6, 10, 2]))             # "6210"
    print(solution([3, 30, 34, 5, 9]))      # "9534330"