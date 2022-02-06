# Problem Id:  858
# Problem Name:  Mirror Reflection, 镜面反射
# Problem Url:  https://leetcode-cn.com/problems/mirror-reflection/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        k = 0
        for i in range(1,p+1):
            if i*q % p == 0:
                k = i
                break
        if k % 2 == 0:
            return 2
        else:
            if (k*q // p) % 2 == 0:
                return 0
            else:
                return 1