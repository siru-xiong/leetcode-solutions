# Problem Id:  面试题 03.04
# Problem Name:  Implement Queue using Stacks LCCI, 化栈为队
# Problem Url:  https://leetcode-cn.com/problems/implement-queue-using-stacks-lcci/
# Problem Level:  Easy
# Language:  Python3
 
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.rec1 = []
        self.rec2 = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.rec1.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        a = self.peek()
        del self.rec2[-1]
        return a


    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.rec2) > 0:
            return self.rec2[-1]
        else:
            while len(self.rec1) > 0:
                self.rec2.append(self.rec1[-1])
                del self.rec1[-1]
            return self.rec2[-1]



    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.rec1) == 0 and len(self.rec2) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()