# https://school.programmers.co.kr/learn/courses/30/lessons/131127
from collections import Counter


def solution(want, number, discount):
    want_dict = dict(zip(want, number))     # 원하는 제품과 그 수량을 매핑한 딕셔너리 생성
    check_days = 10     # 체크할 기간
    count = 0   # 가능한 날짜 수 카운트

    # 현재 윈도우 내에서 원하는 각 제품의 수량을 추적할 딕셔너리: 초기값은 모두 0으로 설정
    current_window = {product: 0 for product in want}

    # 체크할 기간 크기의 첫 윈도우에 대해 제품 수량을 계산
    for i in range(check_days):
        if discount[i] in current_window:   # 원하는 제품인 경우만 개수 추가
            current_window[discount[i]] += 1

    # 첫 윈도우가 조건을 만족하는지 확인
    if all(current_window[product] >= want_dict[product] for product in want_dict):
        count += 1

    # 슬라이딩 윈도우를 이동시키면서 나머지 부분 확인: (가장 왼쪽 요소 제거), (가장 오른쪽 요소 추가)
    for i in range(len(discount) - check_days):
        # 윈도우에서 빠지는 아이템
        if discount[i] in current_window:
            current_window[discount[i]] -= 1

        # 윈도우에 새로 들어오는 아이템
        if discount[i + check_days] in current_window:
            current_window[discount[i + check_days]] += 1

        # 현재 윈도우가 조건을 만족하는지 확인
        if all(current_window[product] >= want_dict[product] for product in want_dict):
            count += 1

    return count


if __name__ == '__main__':
    print(solution(["banana", "apple", "rice", "pork", "pot"],
                   [3, 2, 2, 2, 1],
                   ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))     # 3
    print(solution(["apple"],
                   [10],
                   ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))    # 0