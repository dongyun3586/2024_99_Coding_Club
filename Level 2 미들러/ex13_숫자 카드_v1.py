# https://www.acmicpc.net/problem/10815

n = int(input())
nums1 = list(map(int, input().split()))
m = int(input())
nums2 = list(map(int, input().split()))

nums1 = sorted(nums1)
nums2 = sorted([(num, idx) for idx, num in enumerate(nums2)])

answer = [0] * len(nums2)
i, j = 0, 0
while i < len(nums1) and j < len(nums2):
    if nums2[j][0] == nums1[i]:
        answer[nums2[j][1]] = 1
        i, j = i + 1, j + 1
    elif nums2[j][0] < nums1[i]:
        j += 1
    else:
        i += 1

print(' '.join(map(str, answer)))