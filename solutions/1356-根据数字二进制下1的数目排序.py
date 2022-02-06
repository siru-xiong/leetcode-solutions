# Problem Id:  1356
# Problem Name:  Sort Integers by The Number of 1 Bits, 根据数字二进制下 1 的数目排序
# Problem Url:  https://leetcode-cn.com/problems/sort-integers-by-the-number-of-1-bits/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def c1(x):
            if x == 0:
                return 0
            else:
                t = 1
                r = 0
                while 2 * t <= x:
                    r = r + 1
                    t = t * 2
                count = 0
                while x > 0:
                    if x >= t:
                        x = x - t
                        t = int(t/2)
                        count = count + 1
                    else:
                        t = int(t/2)
                return count
        
        def cp(x):
            return (c1(x),x)
        return sorted(arr,key = cp)
