# https://school.programmers.co.kr/learn/courses/30/lessons/42839?language=python3
from itertools import permutations


def solution(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # 가능한 모든 숫자 조합을 저장할 set
    number_set = set()

    # 1자리부터 numbers의 길이만큼의 모든 순열 생성
    for i in range(1, len(numbers) + 1):
        # i길이의 순열을 모두 구함
        perms = list(permutations(numbers, i))

        # 각 순열을 숫자로 변환하여 set에 추가
        for perm in perms:
            num = int(''.join(perm))
            number_set.add(num)

    # 만들어진 숫자들 중 소수의 개수를 계산
    prime_count = 0
    for num in number_set:
        if is_prime(num):
            prime_count += 1

    return prime_count


if __name__ == '__main__':
    print(solution("17"))   # 3
    print(solution("011"))  # 2