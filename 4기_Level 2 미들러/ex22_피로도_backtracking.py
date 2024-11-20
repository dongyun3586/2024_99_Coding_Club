# https://school.programmers.co.kr/learn/courses/30/lessons/87946?language=python3

def solution(k, dungeons):
    max_count = 0
    visited = [False] * len(dungeons)

    def dfs(current_hp, count):
        nonlocal max_count
        max_count = max(max_count, count)   # 최대 던전 수 갱신

        # 던전 탐험
        for i in range(len(dungeons)):
            if not visited[i]:  # 아직 방문하지 않은 던전
                required_hp, used_hp = dungeons[i]  # [입장 hp, 소모 hp]
                if current_hp >= required_hp:  # 최소 필요 피로도를 만족할 때
                    visited[i] = True
                    dfs(current_hp - used_hp, count + 1)
                    visited[i] = False  # 탐험 종료 후 상태 복원

    # 탐험 시작
    dfs(k, 0)
    return max_count


if __name__ == '__main__':
    print(solution(80, [[80, 20], [50, 40], [30, 10]]))     # 3
