# Problem Id:  989
# Problem Name:  Add to Array-Form of Integer, 数组形式的整数加法
# Problem Url:  https://leetcode-cn.com/problems/add-to-array-form-of-integer/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        K = [int(list(str(K))[i]) for i in range(len(list(str(K))))]
        result = [0] * (max(len(A),len(K))+1)
        if len(A) > len(K):
            K = [0] *  (len(A)-len(K)) + K
        elif len(K) > len(A):
            A = [0] * (len(K)-len(A)) + A
        i = -1
        temp = 0
        while True:
            if temp == 1:
                result[i] = 1 + A[i] + K[i]
                i = i - 1
                temp = 0
            else:
                result[i] = A[i] + K[i]
                i = i -1

            if result[i+1] > 9:
                result[i+1] = result[i+1] % 10
                temp = 1
            if i < -len(A):
                break
        if temp == 1:
            return [1]+result[1:]
        else:
            return result[1:]
                

