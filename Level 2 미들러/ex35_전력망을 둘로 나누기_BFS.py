# https://school.programmers.co.kr/learn/courses/30/lessons/86971
from collections import deque


def bfs_count(graph, v, n):
    '''연결된 노드의 개수를 세는 함수'''
    visited = [False] * (n + 1)
    queue = deque([v])
    visited[v] = True
    count = 1  # 시작 노드도 포함하므로 1로 시작

    while queue:
        node = queue.popleft()
        for w in graph[node]:
            if not visited[w]:
                visited[w] = True
                queue.append(w)
                count += 1

    return count


def solution(n, wires):
    min_difference = float('inf')  # 최소 차이를 아주 큰 수로 초기화

    # 모든 간선을 하나씩 끊어보기
    for i in range(len(wires)):
        # 그래프 생성
        G = [[] for _ in range(n + 1)]  # 정점이 1번부터 시작하기 때문에 n + 1개 생성

        # i번째 간선을 제외한 나머지로 그래프 생성
        for j in range(len(wires)):
            if i != j:
                v1, v2 = wires[j]
                G[v1].append(v2)
                G[v2].append(v1)

        # 끊어진 그래프의 한 부분에 포함된 정점의 수 계산
        part1_count = bfs_count(G, 1, n)    # 그래프, 정점 숫자, 정점 개수

        # 나머지 그래프에 포함된 정점싀 수 계산
        part2_count = n - part1_count

        # 두 부분의 크기의 차이를 계산
        difference = abs(part1_count - part2_count)

        # 최소 차이 업데이트
        min_difference = min(min_difference, difference)

    return min_difference


if __name__ == '__main__':
    print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))  # 3
    print(solution(4, [[1, 2], [2, 3], [3, 4]]))  # 0
    print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))  # 1
