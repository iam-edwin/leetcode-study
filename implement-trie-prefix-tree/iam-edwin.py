from typing import List, Optional


class Trie:
    def __init__(self, value=""):
        self.value = value
        self.hasLeaf = False
        self.nodes: List[Trie] = []

    def __findNode(self, letter: chr) -> Optional["Trie"]:
        for node in self.nodes:
            if node.value == letter:
                return node

        return None

    def insert(self, word: str) -> None:
        node = self.__findNode(word[0])
        if node is None:
            node = Trie(word[0])
            self.nodes.append(node)

        if len(word) == 1:
            node.hasLeaf = True
            return

        node.insert(word[1:])

    def search(self, word: str) -> bool:
        node = self.__findNode(word[0])
        if node is None:
            return False

        if len(word) == 1:
            if node is None:
                return False
            else:
                return node.hasLeaf

        return node.search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        node = self.__findNode(prefix[0])
        if node is None:
            return False

        if len(prefix) == 1:
            if node is None:
                return False
            else:
                return True

        return node.startsWith(prefix[1:])


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
