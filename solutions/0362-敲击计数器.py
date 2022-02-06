# Problem Id:  362
# Problem Name:  Design Hit Counter, 敲击计数器
# Problem Url:  https://leetcode-cn.com/problems/design-hit-counter/
# Problem Level:  Medium
# Language:  Python3
 
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.rec = {}

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.rec[timestamp] = self.rec.get(timestamp,0) + 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        res = 0
        a = list(self.rec.keys())
        for key in a:
            if timestamp - key < 300:
                res += self.rec[key]
            else:
                del self.rec[key]
        return res


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)