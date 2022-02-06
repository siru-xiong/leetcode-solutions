# Problem Id:  剑指 Offer 21
# Problem Name:  调整数组顺序使奇数位于偶数前面 LCOF, 调整数组顺序使奇数位于偶数前面
# Problem Url:  https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        return sorted(nums,key=lambda x:x%2==0)