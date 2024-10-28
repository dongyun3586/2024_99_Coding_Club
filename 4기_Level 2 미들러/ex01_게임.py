# https://www.acmicpc.net/problem/1072
# X와 Y가 주어졌을 때, 형택이가 게임을 최소 몇 번 더 해야 Z가 변하는지 구하는 프로그램을 작성하시오.

x, y = map(int, input().split())  # 총 게임 횟수, 이긴 게임 횟수


def binary_search(x, y) -> int:
    z = (y * 100) // x  # 현재 승률(소수점 이하 버림)
    answer = -1

    # 추가 게임 수를 결정해야 하므로, left는 0으로 시작하고, right는 매우 큰 값으로 설정해야 한다.
    # 추가로 승리해야 하는 게임 수를 찾고자 하는 것이지, y부터 x까지 탐색하는 것이 아니다.
    left, right = 0, 1_000_000_000     # 이진 탐색 범위 설정

    while left <= right:
        mid = (left + right) // 2
        new_z = ((y + mid) * 100) // (x + mid)  # 새로운 승률 계산(앞으로 모든 게임에서 이긴다고 가정)
        if new_z > z:
            answer = mid        # 승률이 증가한 경우, 현재 mid 값을 저장
            right = mid - 1     # 더 적은 추가 게임으로도 승률 증가가 가능한지 탐색
        else:
            left = mid + 1      # 승률이 아직 증가하지 않으면 더 많은 게임 필요

    return answer


print(binary_search(x, y))

# 탐색이 종료되었을 때 left에 저장된 값이 승률을 변화시키는 최소의 추가 승리 수가 된다.