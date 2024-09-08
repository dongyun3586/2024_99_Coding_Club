# https://school.programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    vowels = ["A", "E", "I", "O", "U"]
    index = 0       # 현재 단어 위치 추적 변수
    found = False   # 목표 단어를 찾았는지 여부를 나타내는 플래그

    def dfs(current_word):      # 현재 단어를 인수로 받아 재귀적으로 단어를 생성
        nonlocal index, found   # index와 found 변수가 함수 외부에 정의된 것을 명시함.

        # 단어의 최대 5를 초과하거나 목표 단어를 찾았으면 return
        if len(current_word) > 5 or found:
            return

        print(current_word)
        if current_word == word:    # 현재 단어가 목표 단어이면 found를 True로 설정하고 return
            found = True
            return

        index += 1  # 새로운 단어가 생성될 때마다 index를 증가시켜 사전 순서에서의 위치를 추적

        # 모음을 추가하여 새로운 단어 생성
        for vowel in vowels:
            dfs(current_word + vowel)   # 모음을 현재 단어에 추가하여 새로운 단어를 생성하고, 다시 dfs를 재귀호출하여 깊이 우선 탐색

    dfs("")         # 빈 문자열에서 시작하여 가능한 모든 단어 조합을 생성
    return index    # 목표 단어의 사전 순서를 반환


if __name__ == "__main__":
    # print(solution("AAAAE"))    # 6
    print(solution('E'))          # 782
    print(solution('I'))          # (781 * 2) + 1 = 1563
    # print(solution("AAAE"))     # 10
    # print(solution("I"))        # 1563
    # print(solution("IEO"))      # 1189