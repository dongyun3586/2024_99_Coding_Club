# https://www.acmicpc.net/problem/10816
from bisect import bisect_left

n = int(input())
card1 = list(map(int, input().split()))
m = int(input())
card2 = list(map(int, input().split()))

card1.sort()

for num in card2:
    idx = bisect_left(card1, num)
    count = 0
    while idx < len(card1) and card1[idx] == num:
        count += 1
        idx += 1
    print(count, end=' ')



"""
# 예제 입력1
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10

# 예제 출력1
3 0 0 1 2 0 0 2
"""



