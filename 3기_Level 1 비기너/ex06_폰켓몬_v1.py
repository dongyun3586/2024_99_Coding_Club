# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    nums.sort()
    answer = 1
    n = len(nums) // 2
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            answer += 1
            if answer == n:
                break
    return answer


if __name__ == '__main__':
    print(solution([3, 1, 2, 3]))           # 2
    print(solution([3, 3, 3, 2, 2, 4]))     # 3
    print(solution([3, 3, 3, 2, 2, 2]))     # 2
