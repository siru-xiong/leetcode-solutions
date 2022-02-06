# Problem Id:  42
# Problem Name:  Trapping Rain Water, 接雨水
# Problem Url:  https://leetcode-cn.com/problems/trapping-rain-water/
# Problem Level:  Hard
# Language:  Python3
 
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0
        mh = float('-inf')
        index = 0
        for i in range(len(height)):
            if height[i] > mh:
                index = i
                mh = height[i]
        
        res = 0
        start = height[0]
        for i in range(index):
            if height[i] > start:
                start = height[i]
            else:
                res += (start-height[i])

        end = height[-1]
        for i in range(len(height)-1,index,-1):
            if height[i] > end:
                end = height[i]
            else:
                res += (end-height[i])
        return res


