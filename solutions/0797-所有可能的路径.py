# Problem Id:  797
# Problem Name:  All Paths From Source to Target, 所有可能的路径
# Problem Url:  https://leetcode-cn.com/problems/all-paths-from-source-to-target/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]], start = 0) -> List[List[int]]:
        if start == len(graph)-1:
            return [[start]]
        elif graph[start] == []:
            return -1
        else:
            res = []
            for i in graph[start]:
                t = self.allPathsSourceTarget(graph,i)
                if t != -1:
                    res = res + [[start]+x for x in t]
            if res == []:
                return -1
            else:
                return res