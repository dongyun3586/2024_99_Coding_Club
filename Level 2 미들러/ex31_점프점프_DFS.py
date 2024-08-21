# https://www.acmicpc.net/problem/14248

def dfs(v):
    visited[v] = True
    count = 1

    # 왼쪽으로 점프
    left = v - distances[v]
    if left >= 0 and not visited[left]:
        count += dfs(left)

    # 오른쪽으로 점프
    right = v + distances[v]
    if right < len(distances) and not visited[right]:
        count += dfs(right)

    return count


n = int(input())    # 돌다리의 돌 개수
distances = list(map(int, input().split()))     # 점프 거리 리스트
start = int(input()) - 1    # 출발점 (0-index로 변환)

visited = [False] * n   # 방문 리스트 초기화

# DFS를 이용하여 방문 가능한 돌들의 개수 계산 및 출력
print(dfs(start))   # dfs(2)