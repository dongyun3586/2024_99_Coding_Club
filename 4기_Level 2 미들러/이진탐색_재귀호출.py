def binary_search_left(arr, target, left, right):
    print(f'binary_search_left({left}, {right})')

    # 종료 조건
    if left > right:
        return left

    mid = (left + right) // 2
    if arr[mid] >= target:
        return binary_search_left(arr, target, left, mid - 1)       # 왼쪽으로 탐색
    else:
        return binary_search_left(arr, target, mid + 1, right)      # 오른쪽으로 탐색


def binary_search_right(arr, target, left=0, right=None):
    print(f'binary_search_left({left}, {right})')

    # 종료 조건
    if left > right:
        return right

    mid = (left + right) // 2
    if arr[mid] <= target:
        return binary_search_right(arr, target, mid + 1, right)     # 오른쪽으로 탐색
    else:
        return binary_search_right(arr, target, left, mid - 1)      # 왼쪽으로 탐색


if __name__ == '__main__':
    arr = [1, 2, 3, 3, 3, 4, 4, 5, 5, 5]
    print(binary_search_left(arr, 3, 0, len(arr)-1))    # Expected output: Index of first occurrence of 3
    print(binary_search_right(arr, 3, 0, len(arr)-1))   # Expected output: Index of last occurrence of 3