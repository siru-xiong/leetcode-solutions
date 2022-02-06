# Problem Id:  LCP 11
# Problem Name:  期望个数统计, 期望个数统计
# Problem Url:  https://leetcode-cn.com/problems/qi-wang-ge-shu-tong-ji/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def expectNumber(self, scores: List[int]) -> int:
        return len(set(scores))