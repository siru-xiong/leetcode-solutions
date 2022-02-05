# Problem Id:  787
# Problem Name:  Cheapest Flights Within K Stops, K 站中转内最便宜的航班
# Problem Url:  https://leetcode-cn.com/problems/cheapest-flights-within-k-stops/
# Problem Level:  Medium
 
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        price = [-1] * (n*n)
        for i in range(len(flights)):
            price[flights[i][0]*n+flights[i][1]] = flights[i][2]
        for i in range(n):
            price[i*n+i] = 0
        result = [-1] * (n*(K+1))
        for i in range(n):
            result[i*(K+1)] = price[src*n +i]
        
        for i in range(1,K+1):
            for j in range(n):
                vmin = float('inf')
                for w in range(n):
                    if result[w*(K+1)+i-1]!= -1 and price[w*n+j]!= -1:
                        if result[w*(K+1)+i-1] + price[w*n+j] < vmin:
                            vmin = result[w*(K+1)+i-1] + price[w*n+j]
                if vmin != float('inf'):
                    result[j*(K+1)+i] = vmin
        return result[dst*(K+1)+K]   

