# Problem Id:  1232
# Problem Name:  Check If It Is a Straight Line, 缀点成线
# Problem Url:  https://leetcode-cn.com/problems/check-if-it-is-a-straight-line/
# Problem Level:  Easy
 
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if coordinates[1][0] - coordinates[0][0] == 0:
            return len(set([k[0] for k in coordinates])) == 1
        else:
            k = (coordinates[1][1] -coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
            b = coordinates[0][1] - coordinates[0][0]*k
            result = True
            for i in range(1,len(coordinates)):
                if (k*coordinates[i][0]+b) != coordinates[i][1]:
                    result = False
                    break
            return result

