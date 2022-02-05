# Problem Id:  1515
# Problem Name:  Best Position for a Service Centre, 服务中心的最佳位置
# Problem Url:  https://leetcode-cn.com/problems/best-position-for-a-service-centre/
# Problem Level:  Hard
 
import scipy.optimize
class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        def f(t):
            return sum([sqrt((t[0]-x)**2+(t[1]-y)**2) for x,y in positions])
        return f(scipy.optimize.minimize(f, [50,50]).x)