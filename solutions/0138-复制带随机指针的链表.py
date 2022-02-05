# Problem Id:  138
# Problem Name:  Copy List with Random Pointer, 复制带随机指针的链表
# Problem Url:  https://leetcode-cn.com/problems/copy-list-with-random-pointer/
# Problem Level:  Medium
 
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = {}
        p = head
        while p:
            dic[p] = Node(x=p.val)
            p = p.next
        dic[None] = None
        q = head
        while q:
            dic[q].next = dic[q.next]
            dic[q].random = dic[q.random]
            q = q.next
        return dic[head]