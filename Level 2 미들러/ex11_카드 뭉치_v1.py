# https://school.programmers.co.kr/learn/courses/30/lessons/159994
from collections import deque


def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)

    for word in goal:
        if cards1 and cards1[0] == word:
            cards1.popleft()
        elif cards2 and cards2[0] == word:
            cards2.popleft()
        else:
            return 'No'

    return 'Yes'



if __name__ == "__main__":
    print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"])) # "Yes"
    print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"])) # "No"