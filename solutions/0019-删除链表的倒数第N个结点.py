# Problem Id:  19
# Problem Name:  Remove Nth Node From End of List, 删除链表的倒数第 N 个结点
# Problem Url:  https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
# Problem Level:  Medium
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        re = ListNode(next=head)
        res = re
        save = []
        while res:
            if len(save) < n+1:
                save.append(res)
                res = res.next
            else:
                del save[0]
                save.append(res)
                res = res.next
        save.append(None)
        save[0].next  = save[2]
        return re.next

