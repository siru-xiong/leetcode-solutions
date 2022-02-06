# Problem Id:  985
# Problem Name:  Sum of Even Numbers After Queries, 查询后的偶数和
# Problem Url:  https://leetcode-cn.com/problems/sum-of-even-numbers-after-queries/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        vsum = 0
        for j in range(len(A)):
            if A[j] % 2 == 0:
                vsum = vsum + A[j]
        result.append(vsum)
        for i in range(len(queries)):
            A[queries[i][1]] =  A[queries[i][1]] + queries[i][0]
            if (A[queries[i][1]] - queries[i][0]) % 2 == 0 and A[queries[i][1]] % 2 != 0:
                result.append(result[-1]- A[queries[i][1]] + queries[i][0])
            elif (A[queries[i][1]] - queries[i][0]) % 2 != 0 and A[queries[i][1]] % 2 == 0:
                result.append(result[-1]+ A[queries[i][1]])
            elif (A[queries[i][1]] - queries[i][0]) % 2 == 0 and A[queries[i][1]] % 2 == 0:
                result.append(result[-1]+queries[i][0])
            else:
                result.append(result[-1])
        return result[1:]