# Problem Id:  剑指 Offer II 045
# Problem Name:  二叉树最底层最左边的值, 二叉树最底层最左边的值
# Problem Url:  https://leetcode-cn.com/problems/LwUNpT/
# Problem Level:  Medium
 
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int findDepth(TreeNode* root) {
        if (!root) {
            return 0;
        } else {
            return max(findDepth(root->left),findDepth(root->right))+1;
        }
    }

    int findBottomLeftValue(TreeNode* root) {
        int k = findDepth(root);
        return fb(root,k);
    }

    int fb(TreeNode* root,int m) {
        if ((!root) && (m > 0)) {
            return -999;
        } else if (m == 1) {
            return root->val;
        } else {
            int y = fb(root->left,m-1);
            if (y != -999) {
                return y;
            } else {
                return fb(root->right,m-1);
            }
        }
    }
};