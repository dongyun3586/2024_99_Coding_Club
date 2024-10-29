# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    phone_book.sort()  # 사전순 정렬

    for i in range(len(phone_book) - 1):
        # 현재 번호가 다음 번호의 접두어인지 확인
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False

    return True


if __name__ == '__main__':
    print(solution(["119", "97674223", "1195524421"]))  # false
    print(solution(["123","456","789"]))  # true
    print(solution(["12","123","1235","567","88"]))  # false