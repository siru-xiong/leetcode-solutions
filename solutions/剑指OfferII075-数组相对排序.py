# Problem Id:  剑指 Offer II 075
# Problem Name:  数组相对排序, 数组相对排序
# Problem Url:  https://leetcode-cn.com/problems/0H97ZC/
# Problem Level:  Easy
 
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        s = {}
        for i in range(len(arr2)):
            s[arr2[i]] = i
        arr1.sort(key=lambda x:(s.get(x,float('inf')),x))
        return arr1