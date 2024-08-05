# https://leetcode.com/problems/prefix-and-suffix-search/description/
from typing import List
'''실패한 코드'''

class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class WordFilter:
    def __init__(self, words: List[str]):
        self.head = Node(None)

        # 접두어부터 모든 단어 처리
        for i, word in enumerate(words):
            curr_node = self.head

            # 삽입할 String 각각의 문자에 대해 자식Node를 만들며 내려간다.
            for c in word:
                # 자식 Node에 같은 문자가 없으면 Node 새로 생성
                if c not in curr_node.children:
                    curr_node.children[c] = Node(c)

                # 같음 문자가 있으면 노드를 따로 생성하지 않고, 해당 노드로 이동
                curr_node = curr_node.children[c]

            # 문자열이 끝난 지점의 노드의 data값에 해당 문자열을 표시
            curr_node.data = (word, i)

    def f(self, pref: str, suff: str) -> int:
        # 1 <= words[i].length <= 7
        current_node = self.head
        current_length = len(pref)
        n = 7 - current_length - len(suff)

        # 접두어로 시작하는지 검사
        for c in pref:
            if c in current_node.children:
                current_node = current_node.children[c]
            else:
                return -1

        def dfs(node, suff):
            if not suff and node.data:
                result.append(node.data[1])
            for w in node.children:
                if suff[0] == w.key:
                    dfs(w, suff[1:])
                else:
                    dfs(w, suff)


        # 접미사로 끝나는지 검사
        result = []
        dfs(current_node, suff)
        print(result)

        return 1


# Your WordFilter object will be instantiated and called as such:
obj = WordFilter(["apple"])
param_1 = obj.f("a", "e")  # // return 0, because the word at index 0 has prefix = "a" and suffix = "e".
print(param_1)