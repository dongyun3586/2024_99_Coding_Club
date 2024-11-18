# https://school.programmers.co.kr/learn/courses/30/lessons/87946?language=python3

def solution(k, dungeons):
    max_dungeons = 0
    visited = [False] * len(dungeons)

    def explore(current_fatigue, count):
        nonlocal max_dungeons
        # 최대 던전 수 갱신
        max_dungeons = max(max_dungeons, count)

        # 던전 탐험
        for i in range(len(dungeons)):
            if not visited[i]:  # 아직 방문하지 않은 던전
                required, cost = dungeons[i]
                if current_fatigue >= required:  # 최소 필요 피로도를 만족할 때
                    visited[i] = True
                    explore(current_fatigue - cost, count + 1)
                    visited[i] = False  # 탐험 종료 후 상태 복원

    # 탐험 시작
    explore(k, 0)
    return max_dungeons


if __name__ == '__main__':
    print(solution(80, [[80, 20], [50, 40], [30, 10]]))     # 3
