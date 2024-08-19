# https://leetcode.com/problems/longest-increasing-subsequence/description/
from typing import List
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            pos = bisect.bisect_left(dp, num)
            if pos < len(dp):
                dp[pos] = num
            else:
                dp.append(num)
        return len(dp)


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
    print(s.lengthOfLIS([0, 1, 0, 3, 2, 3]))            # 4
    print(s.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))         # 1
