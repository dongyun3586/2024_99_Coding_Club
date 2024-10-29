# https://school.programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    answer = True

    count_p = 0
    count_y = 0
    for c in s:
        if c == 'p' or c == 'P':
            count_p += 1
        elif c == 'y' or c == 'Y':
            count_y += 1

    return count_p == count_y


if __name__ == '__main__':
    print(solution("pPoooyY"))  # true
    print(solution("Pyy"))      # false