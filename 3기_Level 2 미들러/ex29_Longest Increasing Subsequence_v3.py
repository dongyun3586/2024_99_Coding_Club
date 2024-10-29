# https://leetcode.com/problems/longest-increasing-subsequence/description/
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        n = len(nums)
        dp = [1] * n
        prev = [-1] * n  # 이전 인덱스를 추적하는 배열

        max_len = 0
        max_index = 0

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1   # dp[i]: nums[i]를 마지막 원소로 하는 LIS의 길이
                    prev[i] = j         # 이전 인덱스를 기록
            if dp[i] > max_len:
                max_len = dp[i]
                max_index = i

        # LIS 수열을 역추적
        lis = []
        while max_index != -1:
            lis.append(nums[max_index])
            max_index = prev[max_index]

        return lis[::-1]  # 역추적한 결과를 뒤집어 반환


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # [2, 3, 7, 101]
    print(s.lengthOfLIS([0, 1, 0, 3, 2, 3]))  # [0, 1, 2, 3]
    print(s.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))  # [7]
