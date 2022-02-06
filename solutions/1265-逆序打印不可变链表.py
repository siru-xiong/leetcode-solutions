# Problem Id:  1265
# Problem Name:  Print Immutable Linked List in Reverse, 逆序打印不可变链表
# Problem Url:  https://leetcode-cn.com/problems/print-immutable-linked-list-in-reverse/
# Problem Level:  Medium
# Language:  Python3
 
# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        stack = []
        while head:
            stack.append(head)
            head = head.getNext()
        while stack:
            stack.pop().printValue()