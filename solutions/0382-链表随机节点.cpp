# Problem Id:  382
# Problem Name:  Linked List Random Node, 链表随机节点
# Problem Url:  https://leetcode-cn.com/problems/linked-list-random-node/
# Problem Level:  Medium
 
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
ListNode* rec;
public:
    Solution(ListNode* head) {
        rec = head;
    }
    
    int getRandom() {
        ListNode* start = rec;
        int res = start->val;
        start = start->next;
        int c = 1;
        while (start) {
            c ++;
            if (rand() % c == 0) {
                res = start->val;
            }
            start = start->next;
        }
        return res;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head);
 * int param_1 = obj->getRandom();
 */