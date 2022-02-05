# Problem Id:  593
# Problem Name:  Valid Square, 有效的正方形
# Problem Url:  https://leetcode-cn.com/problems/valid-square/
# Problem Level:  Medium
 
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        r1 = [p2[0]-p1[0],p2[1]-p1[1]]
        r2 = [p3[0]-p1[0],p3[1]-p1[1]]
        r3 = [p4[0]-p1[0],p4[1]-p1[1]]
        r = [r1,r2,r3]
        if r1 == r2 or r2 == r3 or r1 == r3 or [0,0] in r:
            return False
        def n(x):
            return x[0]**2 + x[1]**2
        def cos(x,y):
            return (x[0]*y[0]+x[1]*y[1])**2 / (n(x)*n(y))
        def c(x,y):
            return (x[0]*y[0]+x[1]*y[1]) > 0
        r.sort(key=lambda x: -n(x))
        rn = [n(i) for i in r]
        if (n(r[0]) ==  2*n(r[1]) and n(r[1])==n(r[2]) and r2 != r3):
            if cos(r[0],r[1]) == 1/2 and cos(r[0],r[2]) == 1/2 and c(r[0],r[1]) and c(r[0],r[2]):
                return True
        return False
        