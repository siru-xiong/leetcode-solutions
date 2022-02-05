# Problem Id:  1441
# Problem Name:  Build an Array With Stack Operations, 用栈操作构建数组
# Problem Url:  https://leetcode-cn.com/problems/build-an-array-with-stack-operations/
# Problem Level:  Easy
 
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        index = 0
        for i in range(1,n+1):
            if i < target[index]:
                res.append("Push")
                res.append("Pop")
            elif i == target[index]:
                res.append("Push")
                index = index + 1
            if index >= len(target):
                break
        return res
