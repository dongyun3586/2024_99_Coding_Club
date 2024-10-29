# https://school.programmers.co.kr/learn/courses/30/lessons/178871

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, count):
        self.head = None
        self.tail = None
        self.count = count

    def append(self, data):
        new_node = Node(data)
        if self.head is None:  # 빈 리스트인 경우
            self.head = new_node
            self.tail = new_node
        else:  # 빈 리스트가 아닌 경우
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        return new_node

    def swap_with_pref(self, node):
        prev_node = node.prev               # 이전 노드
        prev_prev_node = prev_node.prev     # 이전 노드의 이전 노드
        next_node = node.next               # 현재 노드의 다음 노드

        # 노드 간 연결 업데이트
        if prev_prev_node is not None:
            prev_prev_node.next = node
        else:
            self.head = node  # 이전 노드가 헤드였을 경우 현재 노드가 헤드가 됨

        if next_node is not None:
            next_node.prev = prev_node
        else:
            self.tail = prev_node  # 현재 노드가 테일인 경우 이전 노드가 테일이 됨

        # 현재 노드와 이전 노드 간의 연결 업데이트
        node.prev = prev_prev_node
        node.next = prev_node
        prev_node.prev = node
        prev_node.next = next_node
        node.data['index'], prev_node.data['index'] = prev_node.data['index'], node.data['index']

    def to_list(self):
        player_list = [0] * self.count
        current = self.head
        while current:
            player_list[current.data['index']] = current.data['name']
            current = current.next
        return player_list


def solution(players, callings):
    # 데이터 전처리: 이름을 쉽게 검색할 수 있도록 이중 연결 리스트와 dict로 전처리

    # 이중 연결 리스트 생성
    dll = DoublyLinkedList(len(players))

    # 이름을 key값으로 한 딕셔너리
    names = {}

    # 노드 추가
    for idx, name in enumerate(players):
        names[name] = dll.append({'index': idx, 'name': name})

    # 해설진이 부른 이름 처리
    for name in callings:
        dll.swap_with_pref(names[name])

    return dll.to_list()


if __name__ == "__main__":
    print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))
    # result: ["mumu", "kai", "mine", "soe", "poe"]
