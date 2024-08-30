# https://leetcode.com/problems/unique-paths/description/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # DP 테이블 초기화
        dp = [[1] * n for _ in range(m)]

        # DP 테이블 채우기
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]



if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3, 2))  # 3
    print(s.uniquePaths(3, 3))  # 6
    print(s.uniquePaths(3, 7))  # 28
