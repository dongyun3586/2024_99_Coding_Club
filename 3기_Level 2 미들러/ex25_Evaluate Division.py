# https://leetcode.com/problems/evaluate-division/
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ...


if __name__ == '__main__':
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    s = Solution()
    print(s.calcEquation(equations, values, queries))  # [6.00000,0.50000,-1.00000,1.00000,-1.00000]

    equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    values = [1.5, 2.5, 5.0]
    queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    print(s.calcEquation(equations, values, queries))  # [3.75000,0.40000,5.00000,0.20000]

    equations = [["a", "b"]]
    values = [0.5]
    queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    print(s.calcEquation(equations, values, queries))  # [0.50000,2.00000,-1.00000,-1.00000]
