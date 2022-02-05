# Problem Id:  1005
# Problem Name:  Maximize Sum Of Array After K Negations, K 次取反后最大化的数组和
# Problem Url:  https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations/
# Problem Level:  Easy
 
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        count = 0
        for i in range(len(A)):
            if A[i] < 0:
                count = count + 1
            else:
                break
        if count >= K:
            return sum(A[K:]) - sum(A[0:K])
        elif (K - count) % 2 ==0:
            return sum(A[count:]) - sum(A[0:count])
        else:
            return max(sum(A[(count+1):]) - sum(A[0:(count+1)]),sum(A[(count-1):]) - sum(A[0:(count-1)]))
