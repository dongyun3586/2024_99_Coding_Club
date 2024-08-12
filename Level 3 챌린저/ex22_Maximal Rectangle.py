# https://leetcode.com/problems/maximal-rectangle/description/
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        r, c = len(matrix), len(matrix[0])
        areas = []

        def dfs(r, c):
            nonlocal area
            matrix[r][c] = '0'
            area += 1

            # 주변 노드 탐색
            for dr, dc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= dr < r and 0 <= dc < c and matrix[dr][dc] == '1':
                    dfs(dr, dc)

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == '1':
                    area = 0
                    dfs(i, j)
                    areas.append(area)


if __name__ == '__main__':
    matrix = [["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]

    print(Solution().maximalRectangle(matrix))  # 6
    print(Solution().maximalRectangle([["0"]]))  # 0
    print(Solution().maximalRectangle([["1"]]))  # 1
