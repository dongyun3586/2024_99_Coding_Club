import heapq


def min_classrooms(lectures):
    # 시작 시간을 기준으로 강의 정렬
    lectures.sort(key=lambda x: x[1])  # x[1]은 시작 시간

    # 최소 힙 초기화
    min_heap = []

    for _, start, end in lectures:
        # 힙의 루트 값(최소 종료 시간)보다 현재 강의의 시작 시간이 크거나 같으면 기존 강의실 사용 가능
        if min_heap and min_heap[0] <= start:
            heapq.heappop(min_heap)  # 기존 강의실 사용 (최소 종료 시간 제거)

        # 현재 강의의 종료 시간을 힙에 추가
        heapq.heappush(min_heap, end)

    # 힙에 남아 있는 요소의 개수가 최소 강의실 수
    return len(min_heap)


# 입력
n = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(n)]

# 출력
print(min_classrooms(lectures))
