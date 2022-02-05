# Problem Id:  1769
# Problem Name:  Minimum Number of Operations to Move All Balls to Each Box, 移动所有球到每个盒子所需的最小操作数
# Problem Url:  https://leetcode-cn.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
# Problem Level:  Medium
 
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = [int(i) for i in list(boxes)]
        left = [0] * len(boxes)
        right = [0] * len(boxes)
        for i in range(1,len(boxes)):
            left[i] = left[i-1] + boxes[i-1]
        for j in range(len(boxes)-2,-1,-1):
            right[j] = right[j+1] + boxes[j+1]
        t = 0
        for i in range(1,len(boxes)):
            t = t + boxes[i]*i
        res = [t]
        for i in range(len(boxes)-1):
            res.append(res[-1] + left[i+1] - right[i])
        return res

