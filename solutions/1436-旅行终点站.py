# Problem Id:  1436
# Problem Name:  Destination City, 旅行终点站
# Problem Url:  https://leetcode-cn.com/problems/destination-city/
# Problem Level:  Easy
 
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return list(set([i[1] for i in paths]) - set([i[0] for i in paths]))[0]