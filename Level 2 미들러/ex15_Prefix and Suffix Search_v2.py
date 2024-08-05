# https://leetcode.com/problems/prefix-and-suffix-search/description/
from typing import List
from collections import defaultdict


class WordFilter:
    def __init__(self, words: List[str]):
        # 두 개의 dict 자료구조를 사용하여 모든 가능한 접두사와 접미사를 전처리
        self.prefix_map = defaultdict(list)
        self.suffix_map = defaultdict(list)

        # 각 단어에 대해 모든 가능한 접두사와 접미사를 추출하여 prefix_map과 suffix_map에 해당 단어이 index와 함께 저장
        for index, word in enumerate(words):
            # 접두사 맵 구성: {"a": [0], "ap": [0], "app": [0], "appl": [0], "apple": [0]}
            for i in range(1, len(word) + 1):
                self.prefix_map[word[:i]].append(index)

            # 접미사 맵 구성: {"apple": [0], "pple": [0], "ple": [0], "le": [0], "e": [0]}
            for i in range(len(word)):
                self.suffix_map[word[i:]].append(index)

    def f(self, pref: str, suff: str) -> int:
        '''
        주어진 접두사 pref와 접미사 suff가 각각 prefix_map과 suffix_map에 존재하는지 확인
        존재하면 prefix_matches와 suffix_matches 리스트에서 가장 큰 공통 인덱스 값을 반환하고,
        존재하지 않으면 -1을 반환한다.
        '''
        if pref in self.prefix_map:     # defaultdict의 key값으로 pref가 존재하는지를 검사하여 한 번에 해당 단어의 index 리스트 탐색
            prefix_matches = self.prefix_map[pref]
        else:
            return -1

        if suff in self.suffix_map:
            suffix_matches = self.suffix_map[suff]
        else:
            return -1

        # prefix_matches와 suffix_matches 리스트에는 index값이 오름차순으로 저장되어 있기 때문에
        # prefix_matches와 suffix_matches 리스트를 역순으로 순회하며 가장 큰 공통 인덱스를 찾는다.
        i, j = len(prefix_matches) - 1, len(suffix_matches) - 1
        while i >= 0 and j >= 0:
            if prefix_matches[i] == suffix_matches[j]:
                return prefix_matches[i]
            elif prefix_matches[i] > suffix_matches[j]:
                i -= 1
            else:
                j -= 1

        return -1   # 공동 인덱스가 없으면 -1 반환


# Your WordFilter object will be instantiated and called as such:
obj = WordFilter(["apple"])
param_1 = obj.f("a", "e")  # // return 0, because the word at index 0 has prefix = "a" and suffix = "e".
print(param_1)