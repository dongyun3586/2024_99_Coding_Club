# https://leetcode.com/problems/find-right-interval/description/
from typing import List
import bisect


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # intervals의 시작점과 인덱스를 함께 저장
        start_points = sorted((start, i) for i, (start, end) in enumerate(intervals))

        result = []
        for start, end in intervals:
            # end 값에 대해 이진 탐색 수행
            idx = bisect.bisect_left(start_points, (end,))

            # 만약 적절한 구간이 있으면 그 인덱스를, 없으면 -1을 추가
            if idx < len(start_points):
                result.append(start_points[idx][1])
            else:
                result.append(-1)

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.findRightInterval([[1, 2]]))  # [-1]
    print(sol.findRightInterval([[3, 4], [2, 3], [1, 2]]))  # [-1,0,1]
    print(sol.findRightInterval([[1, 4], [2, 3], [3, 4]]))  # [-1,2,-1]