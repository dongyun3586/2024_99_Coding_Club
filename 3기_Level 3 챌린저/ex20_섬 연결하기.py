# https://school.programmers.co.kr/learn/courses/30/lessons/42861

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1


def solution(n, costs):
    # 간선 리스트를 가중치 기준으로 오름차순 정렬
    costs.sort(key=lambda x: x[2])

    # 유니온 파인드 구조 초기화
    parent = list(range(n))
    rank = [0] * n

    mst_cost = 0  # 최소 신장 트리의 비용
    edges_used = 0  # 사용된 간선의 수

    # 모든 간선을 순회하며 최소 신장 트리 구성
    for u, v, cost in costs:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst_cost += cost
            edges_used += 1

            # 모든 섬이 연결된 경우
            if edges_used == n - 1:
                break

    return mst_cost


# 예제 입력
n = 4
costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
result = solution(n, costs)
print(result)  # 출력: 4

