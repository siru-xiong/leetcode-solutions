# Problem Id:  23
# Problem Name:  Merge k Sorted Lists, 合并K个升序链表
# Problem Url:  https://leetcode-cn.com/problems/merge-k-sorted-lists/
# Problem Level:  Hard
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists = [i for i in lists if i is not None]
        if len(lists) == 0:
            return None
        index = [0] * len(lists)
        res = ListNode()
        t = res
        while True:
            minv = min([lists[j].val for j in range(len(lists))])
            if minv == float('inf'):
                break
            for i in range(len(lists)):
                if lists[i].val == minv:
                    t.next = ListNode(val=lists[i].val)
                    t = t.next
                    if lists[i].next:
                        lists[i] = lists[i].next
                    else:
                        lists[i].val = float('inf')
        return res.next
