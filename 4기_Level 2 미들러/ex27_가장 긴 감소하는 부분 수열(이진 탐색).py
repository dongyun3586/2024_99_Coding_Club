# https://www.acmicpc.net/problem/11722
import bisect

n = int(input())  # 수열의 크기
arr = list(map(int, input().split()))  # 수열 값


def longest_decreasing_subsequence(n, arr):
    # 수열을 역순으로 뒤집음
    reversed_arr = arr[::-1]

    # LIS 계산을 위한 배열
    lis = []  # LIS를 저장하는 리스트

    # LIS를 계산
    for num in reversed_arr:
        pos = bisect.bisect_left(lis, num)  # 현재 num이 들어갈 위치 찾기
        if pos == len(lis):  # num이 LIS의 끝에 추가될 경우
            lis.append(num)
        else:  # LIS 중간 값을 갱신
            lis[pos] = num

    return len(lis)  # LIS의 길이가 LDS의 길이와 동일


print(longest_decreasing_subsequence(n, arr))
