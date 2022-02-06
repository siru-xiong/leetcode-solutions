# Problem Id:  剑指 Offer 40
# Problem Name:  最小的k个数  LCOF, 最小的k个数
# Problem Url:  https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        if len(arr) <= 1:
            return arr
        elif len(arr) == 2:
            if k == 1:
                return [min(arr[0],arr[1])]
            else:
                return [min(arr[0],arr[1]),max(arr[0],arr[1])]
        else:
            mid = len(arr) // 2
            a = self.getLeastNumbers(arr[:mid],k)
            b = self.getLeastNumbers(arr[mid:],k)
            return self.merge(a,b,k)
    
    def merge(self,arr1,arr2,k):
        res = []
        i = 0
        j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
            if len(res) == k:
                return res
        while i < len(arr1):
            res.append(arr1[i])
            i += 1
            if len(res) == k:
                return res
        while j < len(arr2):
            res.append(arr2[j])
            j += 1
            if len(res) == k:
                return res
        return res
        