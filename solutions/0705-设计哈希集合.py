# Problem Id:  705
# Problem Name:  Design HashSet, 设计哈希集合
# Problem Url:  https://leetcode-cn.com/problems/design-hashset/
# Problem Level:  Easy
# Language:  Python3
 
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.record = set()

    def add(self, key: int) -> None:
        self.record.add(key)

    def remove(self, key: int) -> None:
        if key in self.record:
            self.record.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.record



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)