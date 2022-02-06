# Problem Id:  面试题 16.01
# Problem Name:  Swap Numbers LCCI, 交换数字
# Problem Url:  https://leetcode-cn.com/problems/swap-numbers-lcci/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        numbers[0] = numbers[1] ^ numbers[0]
        numbers[1] = numbers[0] ^ numbers[1]
        numbers[0] = numbers[0] ^ numbers[1]
        return numbers