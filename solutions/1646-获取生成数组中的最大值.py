# Problem Id:  1646
# Problem Name:  Get Maximum in Generated Array, 获取生成数组中的最大值
# Problem Url:  https://leetcode-cn.com/problems/get-maximum-in-generated-array/
# Problem Level:  Easy
 
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            nums = [0,1] + [0] * (n-1)
            i = 1
            t = 1
            while True:
                nums[2*i] = nums[i]
                if 2 * i + 1 <= n:
                    nums[2*i+1] = nums[i] + nums[i+1]
                    t = max(t,nums[i]+nums[i+1])
                t = max(t,nums[i])
                i = i + 1
                if 2*i > n:
                    return t