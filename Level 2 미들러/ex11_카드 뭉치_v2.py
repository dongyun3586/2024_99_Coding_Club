# https://school.programmers.co.kr/learn/courses/30/lessons/159994

def solution(cards1, cards2, goal):
    # 카드 뭉치의 현재 위치를 추적하는 인덱스
    index1, index2 = 0, 0

    # goal의 각 단어를 확인
    for word in goal:
        if index1 < len(cards1) and cards1[index1] == word:
            index1 += 1  # cards1에서 단어를 사용
        elif index2 < len(cards2) and cards2[index2] == word:
            index2 += 1  # cards2에서 단어를 사용
        else:
            return 'No'  # goal의 단어를 만들 수 없는 경우

    return 'Yes'  # 모든 단어를 사용할 수 있는 경우


if __name__ == "__main__":
    print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"])) # "Yes"
    print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"])) # "No"