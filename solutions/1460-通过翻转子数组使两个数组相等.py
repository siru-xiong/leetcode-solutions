# Problem Id:  1460
# Problem Name:  Make Two Arrays Equal by Reversing Sub-arrays, 通过翻转子数组使两个数组相等
# Problem Url:  https://leetcode-cn.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/
# Problem Level:  Easy
 
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        c1 = {}
        c2 = {}
        for i in range(len(target)):
            c1[target[i]] = c1.get(target[i],0) + 1
            c2[arr[i]] = c2.get(arr[i],0) + 1
        for x in c1:
            if c1[x] != c2.get(x,0):
                return False
        return True
