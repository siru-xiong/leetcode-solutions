# Problem Id:  164
# Problem Name:  Maximum Gap, 最大间距
# Problem Url:  https://leetcode-cn.com/problems/maximum-gap/
# Problem Level:  Hard
# Language:  Python3
 
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        vmin = min(nums)
        vmax = max(nums)
        if vmin == vmax:
            return 0
        d = max(1,(vmax-vmin) // (n-1))
        s = (vmax-vmin) // d + 1
        bucket = []
        for i in range(s):
            bucket.append([float('inf'),float('-inf')])
        for i in nums:
            index = (i-vmin) // d
            bucket[index][0] = min(bucket[index][0],i)
            bucket[index][1] = max(bucket[index][1],i)
        i = 0
        prev = -1

        res = float('-inf')
        for i in range(len(bucket)):
            if bucket[i][0] != float('inf'):
                if prev != -1:
                    res = max(res,bucket[i][0]-bucket[prev][1])
                prev = i
        return res