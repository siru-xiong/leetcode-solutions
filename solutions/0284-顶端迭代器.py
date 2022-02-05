# Problem Id:  284
# Problem Name:  Peeking Iterator, 顶端迭代器
# Problem Url:  https://leetcode-cn.com/problems/peeking-iterator/
# Problem Level:  Medium
 
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.t = None
        
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.t:
            self.t = self.iterator.next()
            return self.t
        else:
            return self.t
        
    def next(self):
        """
        :rtype: int
        """
        if not self.t:
            return self.iterator.next()
        else:
            temp = self.t
            self.t = None
            return temp

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.t:
            return True
        else:
            return self.iterator.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].