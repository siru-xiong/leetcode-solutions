# Problem Id:  1122
# Problem Name:  Relative Sort Array, 数组的相对排序
# Problem Url:  https://leetcode-cn.com/problems/relative-sort-array/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        vdict = {}
        for i in range(len(arr2)):
            vdict[arr2[i]] = i
        arr2 = set(arr2)
        def cp(i):
            if i in arr2:
                return (0,vdict[i])
            else:
                return (1,i)
        return sorted(arr1,key=cp)

    

