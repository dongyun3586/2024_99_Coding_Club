# https://www.acmicpc.net/problem/2529
def is_valid(numbers):
    '''주어진 숫자 조합이 부등호 조건을 만족하는지 확인'''
    # 부등호를 하나씩 꺼내서 숫자 쌍이 조건을 만족하는지 검사
    for i in range(len(A)):
        # 부등호가 '<'일 때, 앞의 숫자가 뒤의 숫자보다 작아야 한다
        if A[i] == '<' and numbers[i] > numbers[i + 1]:
            return False
        if A[i] == '>' and numbers[i] < numbers[i + 1]:
            return False
    return True


def find_numbers(current, used):
    '''
    백트래킹을 사용하여 가능한 모든 숫자 조합을 생성하여 results에 저장하는 함수
    :param current: 현재까지 만든 숫자 조합 리스트
    :param used: 0~9의 숫자 중 이미 사용된 숫자를 체크하는 리스트
    '''
    # 종료 조건: current의 길이가 (k+1)이면 숫자 조합이 완성되었음을 의미
    if len(current) == k + 1:
        # 현재 숫자 조합이 부등호 조건을 만족하는지 검사
        if is_valid(current):
            results.append(''.join(map(str, current)))
        return

    # 0~9의 숫자에 대해서 백트래킹을 사용하여 가능한 모든 숫자 조합 생성
    for i in range(10):
        if not used[i]:
            used[i] = True
            current.append(i)
            find_numbers(current, used)
            current.pop()
            used[i] = False


k = int(input())  # 부등호 개수
A = input().strip().split()  # 부등호 순열
results = []  # 가능한 숫자 조합을 저장할 리스트

find_numbers([], [False] * 10)

# 결과 리스트에서 최대값과 최소값 찾아 출력
print(max(results))
print(min(results))
