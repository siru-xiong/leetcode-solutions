# Problem Id:  170
# Problem Name:  Two Sum III - Data structure design, 两数之和 III - 数据结构设计
# Problem Url:  https://leetcode-cn.com/problems/two-sum-iii-data-structure-design/
# Problem Level:  Easy
 
class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.rec = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.rec[number] = self.rec.get(number,0)+1


    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for i in self.rec:
            if value-i in self.rec:
                if (i != value-i) or self.rec[i] == 2:
                    return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)