# https://www.acmicpc.net/problem/14889

def calculate_team_score(team):
    score = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            score += S[team[i]][team[j]]
            score += S[team[j]][team[i]]
    return score


def dfs(index, start_team):
    global min_difference

    # 팀의 절반을 선택했을 경우, 나머지 인덱스를 링크 팀으로 설정
    if len(start_team) == N // 2:
        link_team = [i for i in range(N) if i not in start_team]
        start_score = calculate_team_score(start_team)
        link_score = calculate_team_score(link_team)
        min_difference = min(min_difference, abs(start_score - link_score))
        return

    # 현재 인덱스부터 N까지 재귀적으로 팀을 구성
    for i in range(index, N):
        if i not in start_team:
            start_team.append(i)
            dfs(i + 1, start_team)
            start_team.pop()


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

# 최소 차이 초기화
min_difference = float('inf')

# DFS를 이용해 팀을 나누는 모든 경우 탐색
dfs(0, [])

# 결과 출력
print(min_difference)
