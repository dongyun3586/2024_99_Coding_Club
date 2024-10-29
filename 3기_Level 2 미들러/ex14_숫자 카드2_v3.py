import collections

n = int(input())
counts = collections.Counter(input().split())

m = int(input())
m_nums = input().split()

for i in m_nums:
    print(counts[i], end=' ')

"""
# 예제 입력1
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10

# 예제 출력1
3 0 0 1 2 0 0 2
"""