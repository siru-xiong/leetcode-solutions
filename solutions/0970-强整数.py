# Problem Id:  970
# Problem Name:  Powerful Integers, 强整数
# Problem Url:  https://leetcode-cn.com/problems/powerful-integers/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        xl = []
        if x == 1:
            xl = [1]
        else:
            i = 1
            while i <= bound:
                xl.append(i)
                i = i * x
        yl = []
        if y == 1:
            yl = [1]
        else:
            j = 1
            while j <= bound:
                yl.append(j)
                j = j*y
        result = []
        for i in range(len(xl)):
            for j in range(len(yl)):
                if xl[i] + yl[j] <= bound:
                    result.append(xl[i]+yl[j])
        return list(set(result))