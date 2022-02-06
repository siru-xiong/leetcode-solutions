# Problem Id:  295
# Problem Name:  Find Median from Data Stream, 数据流的中位数
# Problem Url:  https://leetcode-cn.com/problems/find-median-from-data-stream/
# Problem Level:  Hard
# Language:  Python3
 
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.rec = []

    def insert(self,rec,nv):
        if len(rec)==0:
            return [nv]
        else:
            if rec[0] >= nv:
                return [nv]+rec
            elif rec[-1] <= nv:
                return rec+[nv]
            l = 0
            r = len(rec)-1
            while r > l+1:
                mid = (l+r) // 2
                if rec[mid] == nv:
                    return rec[:mid]+[nv]+rec[mid:]
                elif rec[mid] < nv:
                    l = mid
                else:
                    r = mid - 1
            if rec[r] <= nv:
                return rec[:(r+1)]+[nv]+rec[(r+1):]
            else:
                return rec[:(l+1)]+[nv]+rec[(l+1):] 



    def addNum(self, num: int) -> None:
        self.rec = self.insert(self.rec,num)


    def findMedian(self) -> float:
        if len(self.rec) % 2 != 0:
            return self.rec[len(self.rec)//2]
        else:
            return (self.rec[len(self.rec)//2]+self.rec[len(self.rec)//2 - 1])/2.0






# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()