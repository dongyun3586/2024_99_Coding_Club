# https://school.programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    answer = sorted(strings, key=lambda x: (x[n], x))
    return answer


if __name__ == '__main__':
    print(solution(["sun", "bed", "car"], 1))       # ["car", "bed", "sun"]
    print(solution(["abce", "abcd", "cdx"], 2))     # ["abcd", "abce", "cdx"]