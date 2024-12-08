# https://www.acmicpc.net/problem/11722
import bisect


def longest_increasing_subsequence(arr):
    lis = []
    for num in arr:
        # lis 리스트에 num이 들어갈 위치를 찾는다.
        pos = bisect.bisect_left(lis, num)  # num이 삽입될 위치를 찾는다
        if pos == len(lis):
            lis.append(num)
        else:
            lis[pos] = num  # 더 작은 값으로 갱신

    return lis


if __name__ == '__main__':
    print(longest_increasing_subsequence([1, 2, 3, 4, 5, 6]))
    print(longest_increasing_subsequence([1, 2, 3, 7, 5, 6]))
    print(longest_increasing_subsequence([1, 2, 9, 7, 5, 6]))
    print(longest_increasing_subsequence([1, 1, 1, 1, 1, 1]))
