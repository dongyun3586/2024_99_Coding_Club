# https://school.programmers.co.kr/learn/courses/30/lessons/43165
def solution(numbers, target):
    answer = 0

    # dfs 함수는 현재 인덱스와 현재까지의 합계를 인자로 받아 재귀적으로 호출
    def dfs(index, current_sum):
        nonlocal answer
        # index가 numbers의 길이와 같아지면(모든 숫자를 다 사용한 경우)
        if index == len(numbers):
            # current_sum이 target과 같은지 확인하여 같다면 answer를 1 증가
            if current_sum == target:
                answer += 1
            return

        # 현재 index의 숫자를 더하는 경우로 dfs 재귀호출
        dfs(index + 1, current_sum + numbers[index])
        # 현재 index의 숫자를 빼는 경우로 dfs 재귀호출
        dfs(index + 1, current_sum - numbers[index])

    # DFS 탐색 시작
    dfs(0, 0)

    return answer


if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3))  # 5
    print(solution([4, 1, 2, 1], 4))  # 2
