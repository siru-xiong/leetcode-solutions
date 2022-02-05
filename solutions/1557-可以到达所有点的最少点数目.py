# Problem Id:  1557
# Problem Name:  Minimum Number of Vertices to Reach All Nodes, 可以到达所有点的最少点数目
# Problem Url:  https://leetcode-cn.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
# Problem Level:  Medium
 
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        a = set([i[1] for i in edges])
        res = []
        for i in range(n):
            if i not in a:
                res.append(i)
        return res
       
        
