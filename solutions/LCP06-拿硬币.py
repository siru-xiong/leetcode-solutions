# Problem Id:  LCP 06
# Problem Name:  拿硬币, 拿硬币
# Problem Url:  https://leetcode-cn.com/problems/na-ying-bi/
# Problem Level:  Easy
 
class Solution:
    def minCount(self, coins: List[int]) -> int:
        return sum([(i+1) // 2 for i in coins])