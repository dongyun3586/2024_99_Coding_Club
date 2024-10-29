# https://school.programmers.co.kr/learn/courses/30/lessons/42839
'''에라토스테네스의 체를 사용하여 len(numbers) 자리 까지의 소수를 판별한다. '''
import itertools

def solution(numbers):      # numbers는 길이 1 이상 7 이하인 문자열
    # numbers 자리만큼의 숫자에 대해 소수 여부를 판별할 리스트 초기화
    max_num = pow(10, len(numbers))
    is_prime = [True] * max_num
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

    # 2부터 max_num의 제곱근까지 반복
    for num in range(2, int(max_num ** 0.5) + 1):
        if is_prime[num]:
            # number의 배수들을 소수가 아닌 것으로 설정
            for multiple in range(num * num, max_num, num):
                is_prime[multiple] = False


    def backtracking(index, current_subset):
        nonlocal answer
        # 종료 조건: 문자열의 모든 문자에 대해 결정이 끝났을 때
        if index == len(numbers):
            # 현재까지 선택된 부분집합을 결과에 추가
            if current_subset:
                for p in itertools.permutations(current_subset):
                    number = int("".join(p))
                    if is_prime[number] and number not in visited:
                        visited.add(number)
                        answer += 1
            return

        # 현재 문자를 포함하지 않는 경우
        backtracking(index + 1, current_subset)

        # 현재 문자를 포함하는 경우
        current_subset.append(numbers[index])
        backtracking(index + 1, current_subset)

        # 백트래킹: 선택했던 문자 제거
        current_subset.pop()

    answer = 0
    visited = set()
    backtracking(0, [])
    return answer


if __name__ == "__main__":
    print(solution("17"))       # 3
    print(solution("011"))      # 2