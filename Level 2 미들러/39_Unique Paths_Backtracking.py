# https://leetcode.com/problems/unique-paths/description/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.paths = 0  # 인스턴스 변수로 초기화

        def dfs(x, y):
            print(f"dfs({x}, {y})")
            # 종료 조건: 오른쪽 아래 모서리에 도달한 경우
            if x == m - 1 and y == n - 1:
                self.paths += 1
                return

            # 오른쪽으로 이동할 수 있는 경우 재귀 호출
            if y + 1 < n:
                dfs(x, y + 1)

            # 아래로 이동할 수 있는 경우 재귀 호출
            if x + 1 < m:
                dfs(x + 1, y)

        # DFS 호출
        dfs(0, 0)

        return self.paths   # 가능한 모든 경로의 수를 합산하여 반환


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3, 2))  # 3
    print(s.uniquePaths(3, 7))  # 28
