# Problem Id:  933
# Problem Name:  Number of Recent Calls, 最近的请求次数
# Problem Url:  https://leetcode-cn.com/problems/number-of-recent-calls/
# Problem Level:  Easy
 
class RecentCounter:

    def __init__(self):
        self.record = []
        self.left = 0
        self.count = 0


    def ping(self, t: int) -> int:
        self.record.append(t)
        self.count = self.count + 1
        temp = t - 3000
        for i in range(self.left,self.count):
            if self.record[i] >= temp:
                self.left = i
                break
            else:
                i = i + 1
        return self.count-i
        




# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)