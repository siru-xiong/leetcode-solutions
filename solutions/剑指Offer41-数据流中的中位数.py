# Problem Id:  剑指 Offer 41
# Problem Name:  数据流中的中位数  LCOF, 数据流中的中位数
# Problem Url:  https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/
# Problem Level:  Hard
 
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.rec = []


    def addNum(self, num: int) -> None:
        if len(self.rec) == 0:
            self.rec.append(num)
        else:
            l = 0
            r = len(self.rec)-1
            while r - l > 1:
                mid = (l+r) // 2
                if self.rec[mid] < num:
                    l = mid
                elif self.rec[mid] > num:
                    r = mid - 1
                else:
                    l = r = mid
            if self.rec[r] <= num:
                self.rec = self.rec[:(r+1)] + [num] + self.rec[(r+1):]
            elif self.rec[l] <= num:
                self.rec = self.rec[:(l+1)] + [num] + self.rec[(l+1):]
            else:
                self.rec = [num] + self.rec


    def findMedian(self) -> float:
        if len(self.rec) % 2 == 1:
            return self.rec[len(self.rec) // 2]
        else:
            l = len(self.rec) // 2
            return (self.rec[l] + self.rec[l-1])/2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()