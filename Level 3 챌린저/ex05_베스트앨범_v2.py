# https://school.programmers.co.kr/learn/courses/30/lessons/42579

from collections import defaultdict
from heapq import nlargest

def solution(genres, plays):
    answer = []
    genre_dict = defaultdict(lambda: {'play_count': 0, 'songs_count_index': []})

    # 장르별 정보를 genre_dict에 차례대로 저장
    for i in range(len(genres)):
        genre_dict[genres[i]]['play_count'] += plays[i]                     # 장르별 재생 횟수 누적
        genre_dict[genres[i]]['songs_count_index'].append((plays[i], i))    # 장르별 곡별 (재생수, index)

    # 장르별 총 재생 수를 기준으로 내림차순 정렬: [('pop', {'play_count': 3100, 'songs_count_index': [(600, 1), (2500, 4)]}), ()]
    sorted_genres = sorted(genre_dict.items(), key=lambda x: x[1]['play_count'], reverse=True)

    for genre, data in sorted_genres:
        # 노래를 재생 수와 고유 번호를 기준으로 정렬하여 상위 2곡을 선택
        best_two_songs = nlargest(2, data['songs_count_index'], key=lambda x: (x[0], -x[1]))
        answer.extend([song[1] for song in best_two_songs])

    return answer


if __name__ == '__main__':
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    print(solution(genres, plays))      # [4, 1, 3, 0]