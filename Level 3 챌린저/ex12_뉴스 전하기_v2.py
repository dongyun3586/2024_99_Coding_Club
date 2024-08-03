# https://www.acmicpc.net/problem/1135
from collections import defaultdict


def min_time_to_spread_news(n, managers):
    # 트리 구조 생성: 각 상사에게 연결된 부하들을 저장하는 인접 리스트 형태의 딕셔너리
    tree = defaultdict(list)
    # 1번 직원부터 시작해서 모든 직원의 상사 정보를 처리한다. 민식이(0번)는 상사가 없기 때문에 제외시킴.
    for employee in range(1, n):
        manager = managers[employee]
        tree[manager].append(employee)

    # dfs(node)는 현재 노드(node)에서 시작하여 모든 자식 노드에 뉴스를 전파하는 데 필요한 시간을 계산
    def dfs(node):
        times = []  # 현재 노드의 모든 직속 부하에 대한 전파 시간 저장

        # 각 직속 부하에 대해 dfs를 재귀적으로 호출하여 부하들이 뉴스를 듣는 데 걸리는 시간을 계산
        for subordinate in tree[node]:
            times.append(dfs(subordinate))

        # 자식의 전파 시간 중 가장 오래 걸리는 순서대로 정렬
        # 이 정렬은 가장 오래 걸리는 순서대로 뉴스를 전파하기 위한 것
        # 가장 많은 시간이 걸리는 부하에게 먼저 뉴스를 전파하면 전체 전파 시간이 최소화된다.
        times.sort(reverse=True)

        # max_time 변수를 통해 현재 노드의 모든 부하에게 뉴스를 전파하는 데 걸리는 최소 시간을 계산
        max_time = 0
        for i, time in enumerate(times):
            max_time = max(max_time, time + i + 1)  # i+1은 통화 순서에 따른 시간 증가

        return max_time

    # DFS 탐색을 루트 노드(민식이)에서 시작하여 전체 조직 트리를 탐색한다.
    # dfs(0)의 결과로 모든 직원에게 뉴스를 전파하는 데 필요한 최소 시간이 반환된다.
    return dfs(0)

# n = int(input())
# numbers = list(map(int, input().split()))   # -1 0 0
# print(min_time_to_spread_news(n, numbers))

# 예제 입력
print(min_time_to_spread_news(3, [-1, 0, 0]))  # 2
print(min_time_to_spread_news(5, [-1, 0, 0, 2, 2]))  # 3
print(min_time_to_spread_news(5, [-1, 0, 1, 2, 3]))  # 4
print(min_time_to_spread_news(24, [-1, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7, 8, 12, 13, 14, 16, 16, 16]))  # 7
