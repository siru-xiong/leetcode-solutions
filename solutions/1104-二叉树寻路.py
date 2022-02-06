# Problem Id:  1104
# Problem Name:  Path In Zigzag Labelled Binary Tree, 二叉树寻路
# Problem Url:  https://leetcode-cn.com/problems/path-in-zigzag-labelled-binary-tree/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        if label == 1:
            return [1]
        elif label <= 3:
            return [1,label]
        else:
            m = len(bin(label)) - 2
            start = 1 << (m-1)
            t = (label - start + 2) >> 1
            prev_start = start >> 1
            prev_end = start - 1
            prev = prev_end - t + 1
            return self.pathInZigZagTree(prev)+[label]


