# Problem Id:  905
# Problem Name:  Sort Array By Parity, 按奇偶排序数组
# Problem Url:  https://leetcode-cn.com/problems/sort-array-by-parity/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i = 0
        length = len(A)
        count = 0
        while count < length + 1 and i < len(A):
            if A[i] % 2 == 1:
                A.append(A[i])
                del A[i]
                count = count + 1
            else:
                i = i + 1
                count = count + 1
        return A