# https://www.acmicpc.net/problem/25195
import sys

sys.setrecursionlimit(10 ** 6)  # Python의 기본 재귀 깊이 제한은 약 1000회
input = sys.stdin.readline

n, m = map(int, input().split())  # 정점의 수, 간선의 수

# 정방향 그래프 생성
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

k = int(input())  # 팬클럽 수
fanclub_nodes = set(map(int, input().split()))  # 팬클럽이 있는 정점의 번호

# 위 플래그 변수는 모든 경로 중 팬클럽에 도달하지 않는 경로가 하나라도 있으면 False로 변경
found_fanclub_on_all_paths = True  # 모든 경로가 팬클럽에 도달하는지를 확인하는 플래그 전역 변수

# DFS를 통해 리프 노드까지의 모든 경로를 확인
def dfs(graph, v, visited):
    global found_fanclub_on_all_paths

    #  현재 노드가 팬클럽 노드면 True 반환: set 자료구조를 사용하여 팬클럽 노드 확인을 효율적으로 수행
    if v in fanclub_nodes:
        return True

    visited[v] = True
    reach_fanclub = False  # 현재 경로에서 팬클럽에 도달했는지 여부

    # 현재 노드에서 갈 수 있는 모든 경로 탐색
    for w in graph[v]:
        if not visited[w]:  # 방문하지 않은 경로만 탐색
            if dfs(graph, w, visited):
                reach_fanclub = True
            else:
                return False

    # 팬클럽을 만나지 않는 경로 발견 시 플래그 변수를 False로 설정
    if not reach_fanclub:
        found_fanclub_on_all_paths = False
        return False    # 더 이상 탐색할 필요가 없으므로 즉시 종료

    return reach_fanclub


# 1번 정점에서 DFS 탐색을 시작
visited = [False] * (n + 1)
dfs(graph, 1, visited)

# found_fanclub_on_all_paths가 True라면 모든 경로가 팬클럽에 도달한 경우이므로 "Yes"를 출력
if found_fanclub_on_all_paths:
    print("Yes")
else:
    print("yes")
