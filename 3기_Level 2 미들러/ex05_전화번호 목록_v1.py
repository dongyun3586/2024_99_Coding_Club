# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def check_prefix(phone_length, phone_set, number):
    phone_set.add(number)
    for l in phone_length:
        if len(number) <= l:
            return False
        elif number[:l] in phone_set:
            return True


def solution(phone_book):
    # 길이 순서로 정렬
    phone_book = sorted(phone_book, key=lambda x: len(x))
    phone_length = sorted(list(set([len(i) for i in phone_book])))
    phone_set = set()
    answer = True

    # 모든 전화번호 접두어 검사
    for number in phone_book:
        # 전화번호 길이별로 접두어가 되는지 검사
        if check_prefix(phone_length, phone_set, number):
            answer = False
            break

    return answer


if __name__ == '__main__':
    print(solution(["119", "97674223", "1195524421"]))  # false
    print(solution(["123","456","789"]))  # true
    print(solution(["12","123","1235","567","88"]))  # false