# Problem Id:  1317
# Problem Name:  Convert Integer to the Sum of Two No-Zero Integers, 将整数转换为两个无零整数的和
# Problem Url:  https://leetcode-cn.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
# Problem Level:  Easy
 
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1,n):
            if '0' not in list(str(i))+list(str(n-i)):
                return [i,n-i]
                break