def solution(n):
    # 정수 n을 문자열로 변환하여 각 자릿수를 리스트로 분리
    digits = list(str(n))
    # 자릿수를 내림차순으로 정렬
    digits.sort(reverse=True)
    # 정렬된 자릿수 리스트를 다시 문자열로 합친 후, 정수로 변환
    return int("".join(digits))


print(solution(118372))     # 873211
