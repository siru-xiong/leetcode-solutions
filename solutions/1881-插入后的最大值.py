# Problem Id:  1881
# Problem Name:  Maximum Value after Insertion, 插入后的最大值
# Problem Url:  https://leetcode-cn.com/problems/maximum-value-after-insertion/
# Problem Level:  Medium
 
class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0] != '-':
            for i in range(len(n)):
                if int(n[i]) < x:
                    return n[:i]+str(x)+n[i:]
            return n+str(x)
        else:
            for i in range(1,len(n)):
                if int(n[i]) > x:
                    return n[:i]+str(x)+n[i:]
            return n+str(x)