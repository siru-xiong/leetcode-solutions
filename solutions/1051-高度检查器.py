# Problem Id:  1051
# Problem Name:  Height Checker, 高度检查器
# Problem Url:  https://leetcode-cn.com/problems/height-checker/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))