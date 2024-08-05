# https://www.acmicpc.net/problem/10816
from collections import defaultdict


n = int(input())
card1 = list(input().split())
m = int(input())
card2 = list(input().split())

D = defaultdict(int)

# 숫자카드1을 딕셔너리로 변환: 각 숫자를 key로 하여 등장 횟수를 value로 저장
for i in card1:
    D[i] += 1

# 숫자카드2의 숫자가 숫자카드1에 몇 번 등장하는지 딕셔너리로 확인
for i in card2:
    print(D[i], end=' ')


"""
# 예제 입력1
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10

# 예제 출력1
3 0 0 1 2 0 0 2
"""



