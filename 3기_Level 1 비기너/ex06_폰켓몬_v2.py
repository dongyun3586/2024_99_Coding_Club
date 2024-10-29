# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    n = len(nums) // 2
    s = set(nums)
    return n if n < len(s) else len(s)


if __name__ == '__main__':
    print(solution([3, 1, 2, 3]))           # 2
    print(solution([3, 3, 3, 2, 2, 4]))     # 3
    print(solution([3, 3, 3, 2, 2, 2]))     # 2
