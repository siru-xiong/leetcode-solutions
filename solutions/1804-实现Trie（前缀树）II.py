# Problem Id:  1804
# Problem Name:  Implement Trie II (Prefix Tree), 实现 Trie （前缀树） II
# Problem Url:  https://leetcode-cn.com/problems/implement-trie-ii-prefix-tree/
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
        node.children['***'] = node.children.get('***',0) + 1


    def countWordsEqualTo(self, word: str) -> int:
        node = self.rec
        for i in word:
            if i not in node.children:
                return 0
            else:
                node = node.children[i]
        return node.children.get('***',0)


    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.rec
        for i in prefix:
            if i not in node.children:
                return 0
            else:
                node = node.children[i]
        return self.counttotal(node)

    def counttotal(self,node):
        res = node.children.get('***',0)
        for i in node.children:
            if i != '***':
                res += self.counttotal(node.children[i])
        return res

    def erase(self, word: str) -> None:
        node = [self.rec]
        for i in word:
            node.append(node[-1].children[i])
        node[-1].children['***'] -= 1
        while len(node) > 1:
            if node[-1].children.get('***',0)==0 and (('***' in node[-1].children and len(node[-1].children) == 1) or ('***' not in node[-1].children and len(node[-1].children) == 0)):
                t = node[-1].val
                del node[-1]
                del node[-1].children[t]
            else:
                break



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)