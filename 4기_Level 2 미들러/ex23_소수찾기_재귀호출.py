# https://school.programmers.co.kr/learn/courses/30/lessons/42839?language=python3
def solution(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def make_combinations(current, remaining_numbers, used):
        # 현재 만든 숫자를 결과 집합에 추가
        if current:
            primes.add(int(current))

        # 남은 숫자들로 새로운 조합 만들기
        for i in range(len(numbers)):
            if not used[i]:  # 아직 사용하지 않은 숫자라면
                used[i] = True  # 사용 표시
                # 현재 숫자에 새로운 숫자를 붙여서 재귀 호출
                make_combinations(current + numbers[i], remaining_numbers - 1, used)
                used[i] = False  # 백트래킹

    primes = set()  # 만들어진 모든 숫자를 저장할 집합
    used = [False] * len(numbers)  # 각 자리 숫자의 사용 여부를 추적

    # 가능한 모든 조합 만들기
    make_combinations("", len(numbers), used)

    # 소수 개수 계산
    return sum(1 for num in primes if is_prime(num))


if __name__ == '__main__':
    print(solution("17"))   # 3
    print(solution("011"))  # 2