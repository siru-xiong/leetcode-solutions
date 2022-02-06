# Problem Id:  961
# Problem Name:  N-Repeated Element in Size 2N Array, 在长度 2N 的数组中找出重复 N 次的元素
# Problem Url:  https://leetcode-cn.com/problems/n-repeated-element-in-size-2n-array/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        count = {}
        for i in range(len(A)):
            count[A[i]] = count.get(A[i],0) + 1
            if count[A[i]] > 1:
                return A[i]
                break