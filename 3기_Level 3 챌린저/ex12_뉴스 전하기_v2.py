# https://www.acmicpc.net/problem/1135
from collections import defaultdict


def min_time_to_spread_news(n, managers):
    # 트리 생성: 각 상사에게 연결된 부하들을 저장하는 인접 리스트 형태의 딕셔너리
    tree = defaultdict(list)
    for employee in range(1, n):        # 1번 직원부터 시작해서 모든 직원의 상사 정보를 인접리스트 형태로 저장(0번은 상사가 없기 때문에 제외)
        manager = managers[employee]    # 현재 employee 직원의 상사 정보를 가져와 manager 변수에 저장하기
        tree[manager].append(employee)  # tree에 상사 key값에 부하 직원 번호 저장

    # dfs(node)는 현재 노드(node)에서 시작하여 모든 자식 노드에 뉴스를 전파하는 데 필요한 시간을 계산
    def dfs(node):
        times = []  # 현재 노드의 모든 직속 부하에 대한 전파 시간 저장

        # 각 직속 부하에 대해 dfs(node)를 재귀적으로 호출: leaf node부터 위로 올라오면서 처리
        for subordinate in tree[node]:
            times.append(dfs(subordinate))

        # 오래 걸리는 순서대로 뉴스를 전파하기 위해 전파 시간 중 가장 오래 걸리는 순서대로 정렬
        times.sort(reverse=True)

        # 오래 걸리는 뉴스 순서대로 현재노드의 전파 시간을 계산하여, 그 중 가장 긴 시간을 max_time에 저장
        max_time = 0    # 가장 오래 걸리는 뉴스 시간 저장 변수(0으로 초기화)
        for i, time in enumerate(times):
            max_time = max(max_time, time + i + 1)  # time은 서브트리 시간, i+1은 현 노드에서 걸리는 시간
        return max_time

    return dfs(0)   # 루트 노드(민식이)에서 시작하여 전체 조직 트리를 탐색

n = int(input())
numbers = list(map(int, input().split()))   # -1 0 0
print(min_time_to_spread_news(n, numbers))

# 샘플 케이스 테스트
print(min_time_to_spread_news(3, [-1, 0, 0]))  # 2
print(min_time_to_spread_news(5, [-1, 0, 0, 2, 2]))  # 3
print(min_time_to_spread_news(5, [-1, 0, 1, 2, 3]))  # 4
print(min_time_to_spread_news(24, [-1, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7, 8, 12, 13, 14, 16, 16, 16]))  # 7
