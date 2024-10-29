# https://school.programmers.co.kr/learn/courses/30/lessons/160586

def solution(keymap, targets):
    # 각 문자가 입력되기 위한 최소 키 누름 횟수를 저장할 딕셔너리
    min_presses = {}

    # keymap을 순회하면서 최소 키 누름 횟수를 계산
    for idx, keys in enumerate(keymap):
        for i, char in enumerate(keys):
            if char in min_presses:
                min_presses[char] = min(min_presses[char], i + 1)
            else:
                min_presses[char] = i + 1

    # 결과를 저장할 리스트
    result = []

    # 각 target 문자열에 대해 키 누름 횟수를 계산
    for target in targets:
        total_presses = 0
        for char in target:
            if char in min_presses:
                total_presses += min_presses[char]
            else:
                total_presses = -1
                break
        result.append(total_presses)

    return result


if __name__ == '__main__':
    print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"]))        # [9, 4]
    print(solution(["AA"], ["B"]))                              # [-1]
    print(solution(["AGZ", "BSSS"], ["ASA","BGZ"]))             # [4, 6]