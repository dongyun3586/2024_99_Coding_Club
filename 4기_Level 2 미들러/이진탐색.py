def binary_search_left(arr, target):
    '''
    배열에서 target과 같거나 큰 값이 나타나는 가장 왼쪽 위치를 찾기 위한 함수
    mid 위치의 값이 target과 같아도 배열의 왼쪽 부분을 계속 탐색하여 target이 처음으로 나타나는 위치를 찾는다.
    '''
    left, right = 0, len(arr)-1     # left와 right는 배열의 인덱스 범위 전체에 걸쳐 초기화
    while left <= right:
        mid = (left + right)//2
        if target <= arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
        print(f'mid={mid}, left={left}, right={right}')

    return left


def binary_search_right(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right)//2
        if target >= arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
        print(f'mid={mid}, left={left}, right={right}')
    return right


if __name__ == '__main__':
    arr = [1, 2, 3, 3, 3, 4, 4, 5, 5, 5]
    print(binary_search_left(arr, 3))
    print(binary_search_right(arr, 3))