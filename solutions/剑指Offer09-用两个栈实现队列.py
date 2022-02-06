# Problem Id:  剑指 Offer 09
# Problem Name:  用两个栈实现队列 LCOF, 用两个栈实现队列
# Problem Url:  https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/
# Problem Level:  Easy
# Language:  Python3
 
class CQueue:

    def __init__(self):
        self.i = []
        self.o = []


    def appendTail(self, value: int) -> None:
        self.i.append(value)


    def deleteHead(self) -> int:
        if len(self.i) == 0 and len(self.o) == 0:
            return -1
        elif len(self.o) != 0:
            x = self.o[-1]
            del self.o[-1]
            return x
        else:
            while len(self.i) > 0:
                self.o.append(self.i[-1])
                del self.i[-1]
            x = self.o[-1]
            del self.o[-1]
            return x



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()