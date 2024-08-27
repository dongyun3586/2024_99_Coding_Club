# https://www.acmicpc.net/problem/1339
from collections import defaultdict


N = int(input())
words = [input().strip() for _ in range(N)]

# 알파벳 가중치를 저장할 딕셔너리
weight = defaultdict(int)

# 각 알파벳의 가중치 계산
for word in words:
    length = len(word)
    for i in range(len(word)):
        weight[word[i]] += (length - i - 1) ** 10   # 맨 앞의 알파벳부터 높은 가중치 부여

# 가중치에 따라 알파벳 내림차순 정렬
sorted_weight = sorted(weight.items(), key=lambda x: x[1], reverse=True)

# 높은 가중치를 가진 알파벳에 9부터 할당
alpha_to_digit = {}
num = 9
for alpha, _ in sorted_weight:
    alpha_to_digit[alpha] = num
    num -= 1

# 각 단어를 숫자로 변환하여 합 계산
total_sum = 0
for word in words:
    total_sum += int(''.join(str(alpha_to_digit[c]) for c in word))

# 결과 출력
print(total_sum)