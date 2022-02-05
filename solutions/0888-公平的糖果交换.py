# Problem Id:  888
# Problem Name:  Fair Candy Swap, 公平的糖果交换
# Problem Url:  https://leetcode-cn.com/problems/fair-candy-swap/
# Problem Level:  Easy
 
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        B.sort()
        sum1 = sum(A)
        sum2 = sum(B)
        i = 0
        j = 0
        while True:
            if sum1 - sum2 > 2*A[i] - 2*B[j]:
                i = i + 1
            elif sum1 - sum2 < 2*A[i] - 2*B[j]:
                j = j + 1
            else:
                return [A[i],B[j]]
                break