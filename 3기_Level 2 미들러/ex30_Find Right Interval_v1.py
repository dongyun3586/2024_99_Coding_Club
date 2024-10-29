# https://leetcode.com/problems/find-right-interval/description/
from typing import List
from bisect import bisect_left


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # intervals의 각 리스트에 초기 index값 추가
        for i in range(len(intervals)):
            intervals[i].append(i)

        # start값으로 정렬: intervals는 순서대로 처리되어야 하므로 별도의 정렬된 리스트 생성
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        start_list = [i[0] for i in sorted_intervals]   # 정렬된 시작 구간
        idx_list = [i[2] for i in sorted_intervals]     # 정렬된 리스트의 index 위치

        # 모든 구간 반복 처리
        answer = []
        for i in range(len(intervals)):
            end = intervals[i][1]                       # end 값
            position = bisect_left(start_list, end)     # 정렬된 시작 구간 리스트에서 end값이 삽입될 수 있는 위치를 찾음
            # 찾은 위치가 범위를 벗어나지 않는 경우 해당 위치의 index값 저장
            if position < len(idx_list):
                answer.append(idx_list[position])
            else:   # 찾은 위치가 시작 구간 리스트의 마지막 부분인 경우
                answer.append(-1)

        return answer


if __name__ == '__main__':
    sol = Solution()
    print(sol.findRightInterval([[1, 2]]))  # [-1]
    print(sol.findRightInterval([[3, 4], [2, 3], [1, 2]]))  # [-1,0,1]
    print(sol.findRightInterval([[1, 4], [2, 3], [3, 4]]))  # [-1,2,-1]
