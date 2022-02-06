# Problem Id:  973
# Problem Name:  K Closest Points to Origin, 最接近原点的 K 个点
# Problem Url:  https://leetcode-cn.com/problems/k-closest-points-to-origin/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x:x[0]**2+x[1]**2)
        return points[:k]