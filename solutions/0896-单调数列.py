# Problem Id:  896
# Problem Name:  Monotonic Array, 单调数列
# Problem Url:  https://leetcode-cn.com/problems/monotonic-array/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) == 1 or len(A) == 2:
            return True
        else:
            result = True
            index = 0
            up = -1
            for i in range(1,len(A)):
                if A[i] != A[0]:
                    if A[i] > A[0]:
                        up = 1
                    else:
                        up = 0
                    break
            if up == -1:
                return True
            else:
                if up == 1:
                    for i in range(1,len(A)):
                        if A[i] < A[i-1]:
                            result = False
                else:
                    for i in range(1,len(A)):
                        if A[i] > A[i-1]:
                            result = False
                return result
