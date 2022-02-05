# Problem Id:  922
# Problem Name:  Sort Array By Parity II, 按奇偶排序数组 II
# Problem Url:  https://leetcode-cn.com/problems/sort-array-by-parity-ii/
# Problem Level:  Easy
 
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                even.append(A[i])
            else:
                odd.append(A[i])
        A = []
        i = 0
        j = 0
        for i in range(len(odd)):
            A.append(even[i])
            A.append(odd[i])
        return A