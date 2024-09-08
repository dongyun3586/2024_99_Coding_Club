# https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/description/
from typing import List
''' 시간 초과 발생'''

class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nextVisit)

        # 초기 설정
        day = 0
        current_room = 0
        visited_count = [0] * n  # 각 방의 방문 횟수
        visited_count[0] = 1  # 방 0은 첫날 방문

        rooms_visited = 1  # 방 0을 방문한 상태로 시작

        while rooms_visited < n:
            if visited_count[current_room] % 2 == 1:
                # 현재 방문 횟수가 홀수인 경우
                next_room = nextVisit[current_room]
            else:
                # 현재 방문 횟수가 짝수인 경우
                next_room = (current_room + 1) % n

            visited_count[next_room] += 1
            day += 1
            current_room = next_room

            # 새롭게 방을 방문했을 경우
            if visited_count[current_room] == 1:
                rooms_visited += 1

        return day % MOD


if __name__ == '__main__':
    s = Solution()
    print(s.firstDayBeenInAllRooms([0, 0]))     # 2
    print(s.firstDayBeenInAllRooms([0, 0, 2]))  # 6
    print(s.firstDayBeenInAllRooms([0, 1, 2, 0]))   # 6