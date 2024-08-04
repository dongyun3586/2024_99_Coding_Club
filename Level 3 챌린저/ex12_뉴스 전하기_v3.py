# https://www.acmicpc.net/problem/1135

def min_time_to_spread_news(n, managers):
    # 트리 생성
    tree = [[] for _ in range(n)]
    for i in range(1, n):
        tree[managers[i]].append(i)

    times = [0] * n  # time[i] = i번재 노드를 root로 하는 subtree에 뉴스를 전달하는데 필요한 최대 시간

    def dfs(v):
        children_times = []

        for w in tree[v]:  # 내 부하들을 대상으로
            dfs(w)  # Leaf까지 내려감
            children_times.append(times[w])  # 각 child를 root로 하는 subtree에 정보 전달하는데 걸리는 시간 모음

        # 자식이 없으면(빈 리스트 이면) 0
        if not tree[v]:
            children_times.append(0)

        # 자식들중 뉴스를 전파하는 시간이 오래 걸리는 순으로 정렬
        children_times.sort(reverse=True)  # 시간 정보를 담은 리스트를 정렬

        # 시간이 오래 걸리는 쪽부터 먼저 전화를 돌리기
        # 서브트리에 전파하는 시간 + 이번 단계에서 걸리는 시간(i+1) : 첫번쨰 친구는 1 두번째 친구는 2.. n번째 친구는 n
        need_times = [children_times[i] + i + 1 for i in range(len(children_times))]
        times[v] = max(need_times)  # 그 중에 가장 오래 걸리는 시간을 assign

    dfs(0)
    print(times[0] - 1)  # Root node에 정보 전달하는 시간은 없으니 1빼기

# 입력값 받기
n = int(input())
managers = list(map(int, input().split()))
min_time_to_spread_news(n, managers)

min_time_to_spread_news(3, [-1, 0, 0])        # 2
min_time_to_spread_news(5, [-1, 0, 0, 2, 2])  # 3
min_time_to_spread_news(5, [-1, 0, 1, 2, 3])  # 4
min_time_to_spread_news(24, [-1, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7, 8, 12, 13, 14, 16, 16, 16])  # 7