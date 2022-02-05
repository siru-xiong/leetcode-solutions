# Problem Id:  面试题 01.09
# Problem Name:  String Rotation LCCI, 字符串轮转
# Problem Url:  https://leetcode-cn.com/problems/string-rotation-lcci/
# Problem Level:  Easy
 
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if len(s1)+len(s2) == 0:
            return True
        if len(s1) != len(s2):
            return False
        s1 = s1 + s1
        for i in range(len(s1)//2):
            if s1[i] == s2[0]:
                ind = 1
                for j in range(len(s2)):
                    if s1[i+j] != s2[j]:
                        ind = -1
                        break
                if ind == 1:
                    return True
                    
        return False
