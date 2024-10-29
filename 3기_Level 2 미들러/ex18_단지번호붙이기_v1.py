# https://www.acmicpc.net/problem/2667
n = int(input())  # 지도의 크기
A = [[i for i in input()] for _ in range(n)]
visited = [[False] * n for _ in range(n)]
result = []     # 단지별 집의 개수 저장 리스트


def dfs(x, y):
    global count
    if visited[x][y]:
        return
    visited[x][y] = True

    if A[x][y] == '1':
        count += 1
        for dx, dy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= dx < n and 0 <= dy < n and not visited[dx][dy] and A[dx][dy] == '1':
                dfs(dx, dy)


for i in range(n):
    for j in range(n):
        if A[i][j] == '1' and not visited[i][j]:
            count = 0
            dfs(i, j)
            result.append(count)

print(len(result))  # 단지 수 출력
result.sort()       # 각 단지내 집의 수를 오름차순으로 정렬
for i in result:
    print(i)

"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""
