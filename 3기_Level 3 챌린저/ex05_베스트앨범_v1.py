# https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    D = {}
    for name in set(genres):
        D[name] = {'play_count': 0, 'songs': []}    # songs: (count, index)

    for i in range(len(genres)):
        D[genres[i]]['play_count'] += plays[i]  # 장르별 재생 횟수 계산
        # 재생 횟수가 많은 2개의 노래와 비교
        n = len(D[genres[i]]['songs'])
        if n == 2:
            if plays[i] > D[genres[i]]['songs'][0][0]:
                D[genres[i]]['songs'].insert(0, (plays[i], i))
                D[genres[i]]['songs'].pop()
            elif plays[i] > D[genres[i]]['songs'][1][0]:
                D[genres[i]]['songs'][1] = (plays[i], i)
        elif n == 1:
            if plays[i] > D[genres[i]]['songs'][0][0]:
                D[genres[i]]['songs'].insert(0, (plays[i], i))
            else:
                D[genres[i]]['songs'].append((plays[i], i))
        else:
            D[genres[i]]['songs'].append((plays[i], i))

    play_counts = sorted([(data['play_count'], genre) for genre, data in D.items()], reverse=True)

    answer = []
    for idx in play_counts:
        answer += [i[1] for i in D[idx[1]]['songs']]
    return answer


if __name__ == '__main__':
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    print(solution(genres, plays))      # [4, 1, 3, 0]