# Problem Id:  1018
# Problem Name:  Binary Prefix Divisible By 5, 可被 5 整除的二进制前缀
# Problem Url:  https://leetcode-cn.com/problems/binary-prefix-divisible-by-5/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        start = 0
        for i in range(len(A)):
            start = (2 * start + A[i]) % 10
            if start % 5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res