# https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/description/
from typing import List


class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nextVisit)
        dp = [0] * n  # dp[i]는 방 i를 처음 방문할 때까지 걸리는 최소 일 수

        for i in range(1, n):
            dp[i] = (2 * dp[i - 1] + 2 - dp[nextVisit[i]]) % MOD

        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.firstDayBeenInAllRooms([0, 0]))     # 2
    print(s.firstDayBeenInAllRooms([0, 0, 2]))  # 6
    print(s.firstDayBeenInAllRooms([0, 1, 2, 0]))   # 6