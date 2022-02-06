# Problem Id:  1539
# Problem Name:  Kth Missing Positive Number, 第 k 个缺失的正整数
# Problem Url:  https://leetcode-cn.com/problems/kth-missing-positive-number/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        j = 0
        i = 1
        count = 0
        while True:
            if j < len(arr) and i == arr[j]:
                i = i + 1
                j = j + 1
            else:
                count = count + 1
                if count == k:
                    break
                else:
                    i = i + 1
        return i