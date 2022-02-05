# Problem Id:  剑指 Offer 17
# Problem Name:  打印从1到最大的n位数 LCOF, 打印从1到最大的n位数
# Problem Url:  https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/
# Problem Level:  Easy
 
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return list(range(1,10**n))