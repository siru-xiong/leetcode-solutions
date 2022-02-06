# Problem Id:  717
# Problem Name:  1-bit and 2-bit Characters, 1比特与2比特字符
# Problem Url:  https://leetcode-cn.com/problems/1-bit-and-2-bit-characters/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        j = 0
        while True:
            if bits[i] == 0:
                i = i + 1
                j = 0
            else:
                i = i + 2
                j = 1
            if i >= len(bits):
                break
        if j == 0:
            return True
        else:
            return False