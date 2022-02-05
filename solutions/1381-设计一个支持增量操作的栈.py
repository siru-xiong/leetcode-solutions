# Problem Id:  1381
# Problem Name:  Design a Stack With Increment Operation, 设计一个支持增量操作的栈
# Problem Url:  https://leetcode-cn.com/problems/design-a-stack-with-increment-operation/
# Problem Level:  Medium
 
class CustomStack:

    def __init__(self, maxSize: int):
        self.size = maxSize
        self.stack = []
         
    def push(self, x: int) -> None:
        if len(self.stack) < self.size:
            self.stack.append(x)
        
    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack.pop()


    def increment(self, k: int, val: int) -> None:
        k = min(k,len(self.stack))
        for i in range(k):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)