# Problem Id:  2011
# Problem Name:  Final Value of Variable After Performing Operations, 执行操作后的变量值
# Problem Url:  https://leetcode-cn.com/problems/final-value-of-variable-after-performing-operations/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i in operations:
            if i.find('+') >= 0:
                x += 1
            else:
                x -= 1
        return x