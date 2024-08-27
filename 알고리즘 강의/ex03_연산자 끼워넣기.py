# https://www.acmicpc.net/problem/14888

def calculate(oper, a, b):
    # 연산자 oper와 두 숫자 a와 b를 받아서 해당 연산을 수행하고 결과를 반환함.
    if oper == 0:
        return a + b
    elif oper == 1:
        return a - b
    elif oper == 2:
        return a * b
    elif oper == 3:
        if a < 0:   # 음수인 경우 양수로 바꾸어 나눗셈의 몫을 구한 뒤, 다시 음수로 변환하여 결과를 반환
            return -(-a // b)
        else:
            return a // b


def dfs(depth, current_value):
    '''
    모든 가능한 연산자 조합을 탐색하면서 최적의 결과(최댓값과 최솟값)를 찾는다
    :param depth: 현재 연산자의 위치
    :param current_value: 현재까지 계산된 값
    '''
    global max_result, min_result

    # 기저 조건: depth == N - 1인 경우, 모든 숫자를 다 사용한 것이므로 현재 계산된 값이 최종 결과
    if depth == N - 1:
        max_result = max(max_result, current_value)
        min_result = min(min_result, current_value)
        return

    # 백트래킹: 네 종류의 연산자(+, -, *, //)를 순차적으로 사용하면서 모든 가능한 연산자 조합을 탐색
    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1   # 연산자의 개수 1 감소
            next_value = calculate(i, current_value, numbers[depth + 1])
            dfs(depth + 1, next_value)  # 재귀적으로 다음 연산을 수행
            operators[i] += 1   # 연산자를 복구(되돌림)하여 다음 경우의 수를 탐색


N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

# 최댓값과 최솟값 초기화
max_result = -1e9
min_result = 1e9

# 백트래킹 시작
dfs(0, numbers[0])

# 결과 출력
print(max_result)
print(min_result)