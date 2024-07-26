# https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    D = {}
    for name in set(genres):
        D[name] = {'play_count': 0, 'songs': []}    # songs: (count, index)


    for i in range(len(genres)):
        D[genres[i]]['play_count'] += plays[i]  # 장르별 재생 횟수 계산
        # 재생 횟수가 많은 2개의 노래와 비교
        if D[genres[i]]['songs']:
            ...


    answer = []
    return answer


if __name__ == '__main__':
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    print(solution(genres, plays))      # [4, 1, 3, 0]