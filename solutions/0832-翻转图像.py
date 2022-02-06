# Problem Id:  832
# Problem Name:  Flipping an Image, 翻转图像
# Problem Url:  https://leetcode-cn.com/problems/flipping-an-image/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def t(self, b):
        for i in range(len(b)):
            if b[i] == 0:
                b[i] = 1
            else:
                b[i] = 0
        return b

    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[j ^ 1 for j in i[::-1]] for i in A]
        #return [Solution().t(i[::-1]) for i in A]