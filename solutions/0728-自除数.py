# Problem Id:  728
# Problem Name:  Self Dividing Numbers, 自除数
# Problem Url:  https://leetcode-cn.com/problems/self-dividing-numbers/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left,right+1):
            j = [int(k) for k in list(str(i))]
            if 0 in j:
                continue
            result = True
            for x in j:
                if i % x != 0:
                    result = False
                    break
            if result == True:
                res.append(i)
        return res