# https://www.acmicpc.net/problem/10815
import bisect

n = int(input())
nums1 = list(map(int, input().split()))
m = int(input())
nums2 = list(map(int, input().split()))

nums1 = sorted(nums1)

for i in nums2:
    idx = bisect.bisect_left(nums1, i)
    if idx < len(nums1) and nums1[idx] == i:
        print(1, end=' ')
    else:
        print(0, end=' ')


"""
시간 초과
"""

"""
# 예제 입력1
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10

# 예제 출력1
3 0 0 1 2 0 0 2
"""