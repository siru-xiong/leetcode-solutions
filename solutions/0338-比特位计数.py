# Problem Id:  338
# Problem Name:  Counting Bits, 比特位计数
# Problem Url:  https://leetcode-cn.com/problems/counting-bits/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        elif num == 1:
            return [0,1]
        elif num == 2:
            return [0,1,1]
        else:
            res = [0,1,1]
            index = 2
            for i in range(3,num+1):
                if i >= index and i <= (index*2-1):
                    res.append(1+res[i-index])
                else:
                    index = index*2
                    res.append(1)
            return res