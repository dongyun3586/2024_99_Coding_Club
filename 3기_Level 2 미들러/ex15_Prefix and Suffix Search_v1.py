# https://leetcode.com/problems/prefix-and-suffix-search/description/
from typing import List
'''실패한 코드'''


class TrieNode:
    def __init__(self):
        self.children = {}
        self.max_index = -1  # 가장 큰 인덱스를 저장


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, index: int):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.max_index = max(node.max_index, index)  # 해당 노드 경로의 최대 인덱스 갱신

    def search(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return -1
            node = node.children[char]
        return node.max_index


class WordFilter:
    def __init__(self, words: List[str]):
        self.prefix_trie = Trie()
        self.suffix_trie = Trie()

        for index, word in enumerate(words):
            # 접두사와 접미사에 대해 트라이에 단어를 삽입
            self.prefix_trie.insert(word, index)
            self.suffix_trie.insert(word[::-1], index)  # 뒤집힌 단어를 삽입

    def f(self, pref: str, suff: str) -> int:
        # 접두사 검색
        prefix_max_index = self.prefix_trie.search(pref)
        # 접미사 검색 (뒤집힌 접미사 사용)
        suffix_max_index = self.suffix_trie.search(suff[::-1])

        # 두 최대 인덱스 중 가장 큰 공통 인덱스 반환
        if prefix_max_index == -1 or suffix_max_index == -1:
            return -1
        return min(prefix_max_index, suffix_max_index)


# WordFilter 객체 사용 예시
obj = WordFilter(["apple"])
param_1 = obj.f("a", "e")  # 0을 반환해야 함
print(param_1)  # 출력: 0