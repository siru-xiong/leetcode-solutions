# Problem Id:  1337
# Problem Name:  The K Weakest Rows in a Matrix, 矩阵中战斗力最弱的 K 行
# Problem Url:  https://leetcode-cn.com/problems/the-k-weakest-rows-in-a-matrix/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n = len(mat)
        power = [sum(line) for line in mat]
        ans = list(range(n))
        ans.sort(key=lambda i: (power[i], i))
        return ans[:k]