# Problem Id:  981
# Problem Name:  Time Based Key-Value Store, 基于时间的键值存储
# Problem Url:  https://leetcode-cn.com/problems/time-based-key-value-store/
# Problem Level:  Medium
 
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.rec = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.rec:
            self.rec[key].append([value,timestamp])
        else:
            self.rec[key] = [[value,timestamp]]


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.rec:
            return ''
        res = self.rec[key]
        l = 0
        r = len(res) - 1
        while l > r + 1:
            mid = (l+r) // 2
            if res[mid][1] > timestamp:
                r = mid - 1
            else:
                l = mid
        if res[r][1] <= timestamp:
            return res[r][0]
        elif res[l][1] <= timestamp:
            return res[l][0]
        else:
            return ''



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)