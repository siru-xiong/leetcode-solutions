# Problem Id:  96
# Problem Name:  Unique Binary Search Trees, 不同的二叉搜索树
# Problem Url:  https://leetcode-cn.com/problems/unique-binary-search-trees/
# Problem Level:  Medium
 
class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 0:
            return 1
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 5
        else:
            res = [1,1,2,5]
            for i in range(4,n+1):
                temp = 0
                for j in range(i):
                    temp = temp + res[j]*res[i-j-1]
                res.append(temp)
            return res[-1]