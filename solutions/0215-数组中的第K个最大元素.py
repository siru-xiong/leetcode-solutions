# Problem Id:  215
# Problem Name:  Kth Largest Element in an Array, 数组中的第K个最大元素
# Problem Url:  https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
# Problem Level:  Medium
 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = [float('-inf')] * k
        for i in nums:
            for j in range(k):
                if i >= res[j]:
                    res = res[0:j] + [i] + res[j:(-1)]
                    break
        return res[-1]