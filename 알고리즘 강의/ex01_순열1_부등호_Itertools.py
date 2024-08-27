# https://www.acmicpc.net/problem/2529
from itertools import permutations


def is_valid(numbers):
    # 부등호를 하나씩 꺼내서 인접한 두 숫자가 조건을 만족하는지 검사
    for i in range(len(A)):
        if A[i] == '<' and numbers[i] > numbers[i + 1]:
            return False
        if A[i] == '>' and numbers[i] < numbers[i + 1]:
            return False
    return True


k = int(input())  # 부등호 개수
A = input().strip().split()  # 부등호 순열
results = []  # 가능한 숫자 조합을 저장할 리스트

# 0부터 9까지의 숫자 중 (k+1)개의 숫자 조합을 생성
for perm in permutations(range(10), k + 1):
    if is_valid(perm):
        results.append(''.join(map(str, perm)))

# 결과 리스트에서 최대값과 최소값 찾아 출력
print(max(results))
print(min(results))
