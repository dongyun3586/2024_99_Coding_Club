# https://school.programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    n = len(name)
    answer = 0
    min_move = n - 1  # 오른쪽으로 쭉 가는 기본 이동 횟수

    for i in range(n):
        # 현재 알파벳 조작 횟수 계산
        answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)

        # 다음 문자 위치 찾기
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1

        # 좌우 이동 횟수 계산
        # 오른쪽으로 갔다가 돌아오는 경우, 왼쪽으로 갔다가 돌아오는 경우
        min_move = min(min_move, i + i + n - next_idx, i + (n - next_idx) + (n - next_idx))

    answer += min_move
    return answer



if __name__ == "__main__":
    print(solution("JEROEN"))   # 56
    print(solution("JAN"))      # 23