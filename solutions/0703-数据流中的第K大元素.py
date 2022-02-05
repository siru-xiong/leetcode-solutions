# Problem Id:  703
# Problem Name:  Kth Largest Element in a Stream, 数据流中的第 K 大元素
# Problem Url:  https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/
# Problem Level:  Easy
 
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.record = [float('-inf')] * k
        self.length = k
        for i in nums:
            for j in range(k):
                if i >= self.record[j]:
                    self.record = self.record[:j] + [i] + self.record[j:(-1)]
                    break

    def add(self, val: int) -> int:
        for j in range(self.length):
            if val >= self.record[j]:
                self.record = self.record[:j] + [val] + self.record[j:(-1)]
                break
        return self.record[-1]




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)