# https://leetcode.com/problems/prefix-and-suffix-search/description/
from typing import List


class WordFilter:
    def __init__(self, words: List[str]):
        self.prefix_suffix_map = {}

        # 모든 가능한 접두사와 접미사 조합을 인덱스와 함께 저장합니다.
        for index, word in enumerate(words):
            word_len = len(word)
            for i in range(word_len + 1):  # 0부터 len(word)까지
                for j in range(word_len + 1):  # 0부터 len(word)까지
                    prefix = word[:i]
                    suffix = word[j:]
                    # 접두사-접미사 쌍에 대한 인덱스를 저장합니다.
                    self.prefix_suffix_map[(prefix, suffix)] = index

    def f(self, pref: str, suff: str) -> int:
        # 주어진 접두사와 접미사에 대한 가장 큰 인덱스를 반환하거나, 없으면 -1을 반환합니다.
        return self.prefix_suffix_map.get((pref, suff), -1)


# WordFilter 객체는 다음과 같이 생성 및 호출됩니다:
obj = WordFilter(["apple"])
param_1 = obj.f("a", "e")  # 0을 반환해야 합니다.
print(param_1)  # 출력: 0