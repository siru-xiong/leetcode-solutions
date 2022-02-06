# Problem Id:  932
# Problem Name:  Beautiful Array, 漂亮数组
# Problem Url:  https://leetcode-cn.com/problems/beautiful-array/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        if n == 1:
            return [1]
        elif n == 2:
            return [1,2]
        elif n == 3:
            return [1,3,2]
        elif n == 4:
            return [2,1,4,3]
        elif n == 5:
            return [3,1,2,5,4]
        else:
            l = self.beautifulArray((n+1) // 2)
            r = self.beautifulArray(n//2)
            left = [2*i-1 for i in l]
            right = [2*i for i in r]
            return left+right