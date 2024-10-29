# https://leetcode.com/problems/longest-increasing-subsequence/description/
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 각 숫자 하나만으로도 증가 부분 수열을 만들 수 있으니 모든 dp[i]를 1로 초기화한다.
        dp = [1] * len(nums)

        # dp[i]를 구하기 위해, nums[i] 이전의 모든 요소 nums[j] (j < i)에 대해 확인
        for i in range(len(nums)):
            for j in range(i):
                # 만약 nums[j] 뒤에 nums[i]를 붙여 증가 부분 수열을 만들 수 있다면
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
    print(s.lengthOfLIS([0, 1, 0, 3, 2, 3]))            # 4
    print(s.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))         # 1
