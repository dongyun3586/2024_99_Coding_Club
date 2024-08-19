# https://leetcode.com/problems/missing-number/description/
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        A = [0] * (len(nums) + 1)
        for i in nums:
            A[i] = 1

        for i in range(len(A)):
            if A[i] == 0:
                return i


if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([3, 0, 1]))                    # 2
    print(s.missingNumber([0, 1]))                       # 2
    print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8
