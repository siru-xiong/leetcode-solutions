# Problem Id:  461
# Problem Name:  Hamming Distance, 汉明距离
# Problem Url:  https://leetcode-cn.com/problems/hamming-distance/
# Problem Level:  Easy
 
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')