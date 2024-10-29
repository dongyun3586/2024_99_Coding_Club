# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ''
    is_first = True
    for c in s:
        if is_first and c.isalpha():    # 단어의 첫번째 문자이고, 알파벳인 경우 => 대문자로 변경
            answer += c.upper()
            is_first = False
        elif c.isalpha():               # 단어의 첫번째 문자가 아닌 경우 => 소문자로 변경
            answer += c.lower()
        elif c == ' ':                  # 공백인 경우 => is_first를 True로 변경
            answer += c
            is_first = True
        else:   # 숫자                  # 숫자인 경우 => is_first를 False로 변경
            answer += c
            is_first = False
    return answer


if __name__ == '__main__':
    print(solution('3people unFollowed me'))    # "3people Unfollowed Me"
    print(solution('for the last week'))        # "For The Last Week"