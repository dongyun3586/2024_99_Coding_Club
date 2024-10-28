# https://www.acmicpc.net/problem/11403
def floyd_warshall(n, graph):
    # 플로이드-워셜 알고리즘을 통해 경로의 존재 여부를 계산
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # i에서 j로 직접 가는 길이 있거나, i에서 k를 거쳐 j로 가는 길이 있으면 1로 갱신
                if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                    graph[i][j] = 1

    # 결과 출력
    for row in graph:
        print(" ".join(map(str, row)))

# 입력 처리
n = int(input())  # 정점의 개수
graph = [list(map(int, input().split())) for _ in range(n)]

# 함수 호출 및 결과 출력
floyd_warshall(n, graph)
