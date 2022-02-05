# Problem Id:  1109
# Problem Name:  Corporate Flight Bookings, 航班预订统计
# Problem Url:  https://leetcode-cn.com/problems/corporate-flight-bookings/
# Problem Level:  Medium
 
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n
        for i in bookings:
            res[i[0]-1] += i[2]
            if i[1] < n:
                res[i[1]] -= i[2]
        for i in range(1,len(res)):
            res[i] += res[i-1]
        return res