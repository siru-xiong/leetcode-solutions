# Problem Id:  706
# Problem Name:  Design HashMap, 设计哈希映射
# Problem Url:  https://leetcode-cn.com/problems/design-hashmap/
# Problem Level:  Easy
# Language:  Python3
 
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.record = {}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.record[key] = value
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.record:
            return self.record[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.record:
            del self.record[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)