# Problem Id:  681
# Problem Name:  Next Closest Time, 最近时刻
# Problem Url:  https://leetcode-cn.com/problems/next-closest-time/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def next(self,t1,t2):
        h1 = int(t1[:2])
        h2 = int(t2[:2])
        m1 = int(t1[3:])
        m2 = int(t2[3:])
        if h1 < h2:
            return (h2-h1)*60 + m2 - m1
        elif h1 == h2:
            if m1 <= m2:
                return m2-m1
            else:
                return 24*60 - (m1-m2)
        else:
            return 24*60 - (h1-h2)*60  + (m2-m1)

    def nextClosestTime(self, time: str) -> str:
        t = set(list(time[:2]+time[3:]))
        dist = float('inf')
        res  = ''
        for i1 in t:
            for i2 in t:
                for i3 in t:
                    for i4 in t:
                        h = int(i1+i2)
                        m = int(i3+i4)
                        if h >= 0 and h <= 23 and m >= 0 and m <= 59:
                            d = self.next(time,i1+i2+':'+i3+i4)
                            if d <= dist and d != 0:
                                res = i1+i2+':'+i3+i4
                                dist = d
        if res == '':
            return time
        else:
            return res
