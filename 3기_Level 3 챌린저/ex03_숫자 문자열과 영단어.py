# https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    answer = 0
    D = {'ze': ('zero', 0), 'on': ('one', 1), 'tw': ('two', 2), 'th': ('three', 3), 'fo': ('four', 4),
         'fi': ('five', 5), 'si': ('six', 6), 'se': ('seven', 7), 'ei': ('eight', 8), 'ni': ('nine', 9)}

    i = 0
    while i < len(s):
        if s[i].isdigit():
            answer = answer * 10 + int(s[i])
            i += 1
        else:
            answer = answer * 10 + D[s[i:i + 2]][1]
            i += len(D[s[i:i + 2]][0])

    return answer


if __name__ == '__main__':
    print(solution('one4seveneight'))       # 1478
    print(solution('23four5six7'))          # 234567
    print(solution('2three45sixseven'))     # 234567
    print(solution('123'))                  # 123
