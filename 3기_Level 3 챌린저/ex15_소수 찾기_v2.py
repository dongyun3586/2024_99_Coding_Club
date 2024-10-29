# https://school.programmers.co.kr/learn/courses/30/lessons/42839
'''에라토스테네스의 체를 사용하여 len(numbers) 자리 까지의 소수를 판별한다. '''
import itertools

def solution(numbers):
    # 소수 판별 함수
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    unique_numbers = set()
    # 모든 길이의 순열을 생성하여 소수 판별
    for length in range(1, len(numbers) + 1):
        for permutation in itertools.permutations(numbers, length):
            num = int("".join(permutation))
            if num not in unique_numbers:
                unique_numbers.add(num)

    # 소수의 개수 반환
    return sum(1 for num in unique_numbers if is_prime(num))

if __name__ == "__main__":
    print(solution("17"))       # 3
    print(solution("011"))      # 2