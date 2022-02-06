# Problem Id:  1184
# Problem Name:  Distance Between Bus Stops, 公交站间的距离
# Problem Url:  https://leetcode-cn.com/problems/distance-between-bus-stops/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        start , destination = min(start,destination) , max(start,destination)
        a = sum(distance[start:destination])
        b = sum(distance[:start]+distance[destination:])
        return min(a,b)