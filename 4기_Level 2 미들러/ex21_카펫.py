# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    total_tiles = brown + yellow  # 전체 격자의 수

    # height는 최소 3부터 시작, total_tiles의 제곱근까지 탐색
    for height in range(3, int(total_tiles ** 0.5) + 1):
        if total_tiles % height == 0:  # height가 total_tiles의 약수여야 함
            width = total_tiles // height  # 가로 길이 계산
            # 조건 확인: 중앙의 노란색 크기가 일치하는지
            if (width - 2) * (height - 2) == yellow:
                return [width, height]


if __name__=='__main__':
    print(solution(10, 2))      # [4, 3]
    print(solution(8, 1))       # [3, 3]
    print(solution(24, 24))     # [8, 6]