# https://www.acmicpc.net/problem/17834

n, m = map(int, input().split())    # n: 수풀의 수, m: 오솔길의 수
G = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

