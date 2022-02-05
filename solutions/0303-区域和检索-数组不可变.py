# Problem Id:  303
# Problem Name:  Range Sum Query - Immutable, 区域和检索 - 数组不可变
# Problem Url:  https://leetcode-cn.com/problems/range-sum-query-immutable/
# Problem Level:  Easy
 
class NumArray:

    def __init__(self, nums: List[int]):
        if len(nums) == 0:
            pass
        else:
            self.dp = [0] * len(nums)
            self.dp[0] = nums[0]
            for i in range(1,len(nums)):
                self.dp[i] = self.dp[i-1] + nums[i]


    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.dp[j]
        else:
            return self.dp[j] - self.dp[i-1]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)