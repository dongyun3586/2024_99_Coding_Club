# https://leetcode.com/problems/unique-paths-ii/
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # DP 테이블 초기화
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1] * c for _ in range(r)]

        flag = False
        for i in range(c):
            if obstacleGrid[0][i] == 1:
                flag = True
            if flag:
                dp[0][i] = 0

        flag = False
        for i in range(r):
            if obstacleGrid[i][0] == 1:
                flag = True
            if flag:
                dp[i][0] = 0

        # DP 테이블 채우기
        for i in range(1, r):
            for j in range(1, c):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[r - 1][c - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # 2
    print(s.uniquePathsWithObstacles([[0, 1], [0, 0]]))  # 1
    print(s.uniquePathsWithObstacles([[1, 0]]))  # 0
