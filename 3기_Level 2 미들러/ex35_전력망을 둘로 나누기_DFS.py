# https://school.programmers.co.kr/learn/courses/30/lessons/86971
from collections import defaultdict

def dfs(v, visited, graph):
    stack = [v]
    count = 0
    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            count += 1
            for w in graph[current]:
                if not visited[w]:
                    stack.append(w)
    return count

def solution(n, wires):
    min_difference = float('inf')

    for i in range(len(wires)):
        # 그래프 생성
        graph = defaultdict(list)
        for j in range(len(wires)):
            if i != j:
                v1, v2 = wires[j]
                graph[v1].append(v2)
                graph[v2].append(v1)

        # 방문 여부를 기록할 배열
        visited = [False] * (n + 1)

        # 첫 번째 연결 요소 크기 계산
        part1_count = dfs(1, visited, graph)
        part2_count = n - part1_count

        # 두 부분의 크기 차이 계산
        difference = abs(part1_count - part2_count)
        min_difference = min(min_difference, difference)

    return min_difference


if __name__ == '__main__':
    print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))  # 3
    print(solution(4, [[1, 2], [2, 3], [3, 4]]))  # 0
    print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))  # 1
