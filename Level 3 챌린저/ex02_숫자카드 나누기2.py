# https://school.programmers.co.kr/learn/courses/30/lessons/135807
from math import gcd
from functools import reduce


def solution(arrayA, arrayB):
    # 1. 각 리스트의 최대공약수 구하기
    gcdA = reduce(gcd, arrayA)
    gcdB = reduce(gcd, arrayB)

    # 2. 최대공약수가 다른 리스트의 모든 요소를 나눌 수 없는지 확인하기
    resultA = gcdA if all(x % gcdA != 0 for x in arrayB) else 0
    resultB = gcdB if all(x % gcdB != 0 for x in arrayA) else 0

    # 3. 위의 조건을 만족하는 가장 큰 최대공약수 반환하기, 조건을 만족하는 값이 없으면 0 반환
    return max(resultA, resultB)


if __name__=="__main__":
    print(solution([10, 17], [5, 20]))              # 0
    print(solution([10, 20], [5, 17]))              # 10
    print(solution([14, 35, 119], [18, 30, 102]))   # 7
    print(solution([10, 20], [40, 80]))             # 40
    print(solution([10, 20], [15, 45]))             # 15


"""
최대 공약수(GCD)는 주어진 수들의 공통된 약수 중 가장 큰 값이다. 즉, GCD는 리스트의 모든 숫자를 나눌 수 있는 가장 큰 값

리스트의 최대 공약수만을 고려하여 조건을 만족하는 가장 큰 값을 찾을 수 있다. 
각 리스트의 GCD만 구한 후 다른 리스트가 이를 나누는지 여부를 검사하는 방법은 문제의 조건을 효율적으로 만족시키는 방법
GCD가 리스트의 모든 요소를 나눌 수 있는 가장 큰 값이라는 특성을 활용한 것

GCD보다 작은 값은 이미 GCD에 포함되므로, 조건을 만족하는 가장 큰 값이 될 수 없다. 

arrayA의 GCD로 arrayB의 모든 요소를 나눌 때 GCD로는 나눌 수 있고, GCD보다 작은 약수로는 나눌 수 없는 경우는 없다. 
"""