# Problem Id:  208
# Problem Name:  Implement Trie (Prefix Tree), 实现 Trie (前缀树)
# Problem Url:  https://leetcode-cn.com/problems/implement-trie-prefix-tree/
# Problem Level:  Medium
 
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Trie:
    def __init__(self):
        self.rec = Node(val='*',children = {})

    def insert(self, word: str) -> None:
        node = self.rec
        for i in word:
            if i not in node.children:
                node.children[i] = Node(val=i,children = {})
                node = node.children[i]
            else:
                node = node.children[i]
        node.children['***'] = '***'

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.rec
        for i in word:
            if i not in node.children:
                return False
            else:
                node = node.children[i]
        return '***' in node.children


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.rec
        for i in prefix:
            if i not in node.children:
                return False
            else:
                node = node.children[i]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)