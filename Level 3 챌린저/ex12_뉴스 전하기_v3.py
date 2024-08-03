# https://www.acmicpc.net/problem/1135
n = int(input())
t = list(map(int, input().split()))

# 트리 생성
tree = [[] for _ in range(n)]
for idx in range(1, n):
    tree[t[idx]].append(idx)

# time[i] = i번재 노드를 root로 하는 subtree에 뉴스를 전달하는데 필요한 최대 시간
time = [0] * n

def dp(v):
    children_times = []

    for node in tree[v]:               # 내 부하들을 대상으로
        dp(node)                       # Leaf까지 내려감
        children_times.append(time[node])    # 각 child를 root로 하는 subtree에 정보 전달하는데 걸리는 시간 모음

    # child가 없으면 0
    if not tree[v]:
        children_times.append(0)

    # 자식들중 시간이 많이 걸리는 순으로 뉴스를 전달해줘야 전체 시간을 아낄 수 있다.
    children_times.sort(reverse=True) # 시간 정보를 담은 리스트를 정렬

    # 시간이 오래 걸리는 쪽부터 먼저 전화를 돌리기
    # 서브트리에 전파하는 시간 + 이번 단계에서 걸리는 시간(i+1) : 첫번쨰 친구는 1 두번째 친구는 2.. n번째 친구는 n
    need_time = [children_times[i] + i + 1 for i in range(len(children_times))]
    time[v] = max(need_time)  # 그 중에 가장 오래 걸리는 시간을 assign


dp(0)
print(time[0] - 1)  # Root node에 정보 전달하는 시간은 없으니 1빼기