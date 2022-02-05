# Problem Id:  11
# Problem Name:  Container With Most Water, 盛最多水的容器
# Problem Url:  https://leetcode-cn.com/problems/container-with-most-water/
# Problem Level:  Medium
 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        ans = float('-inf')
        while i <= j:
            ans = max(ans,min(height[i],height[j])*(j-i))
            if height[i] <= height[j]:
                i = i + 1
            else:
                j = j - 1
        return ans