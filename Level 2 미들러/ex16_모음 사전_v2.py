# https://school.programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    # 각 자리별 가중치 (5^4, 5^3, 5^2, 5^1, 5^0): 각 자리가 변할 때 사전적으로 얼마나 많은 단어가 앞서 나가는지를 나타낸다.
    weights = [781, 156, 31, 6, 1]  # 계산: 781 = 5^4 + 5^3 + 5^2 + 5^1 + 1
    result = 0   # 주어진 단어가 사전에서 몇 번째에 위치하는지를 저장하는 변수

    # word의 각 문자를 순회하면서 해당 문자가 위치한 자리의 가중치를 사용하여 사전적 위치를 계산
    for i, ch in enumerate(word):
        result += vowels.index(ch)  * weights[i] + 1    # 1을 더하는 이유는 시작 위치가 1이기 때문

    return result


# 예시 테스트 케이스
print(solution("AAAAE"))  # Output: 6
print(solution("AAAE"))  # Output: 10
print(solution("I"))  # Output: 1563
print(solution("EIO"))  # Output: 1189