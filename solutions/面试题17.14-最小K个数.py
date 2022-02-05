# Problem Id:  面试题 17.14
# Problem Name:  Smallest K LCCI, 最小K个数
# Problem Url:  https://leetcode-cn.com/problems/smallest-k-lcci/
# Problem Level:  Medium
 
class Solution:
    def merge(self,left,right):
        i,j=0,0
        res=[]
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
        if i==len(left):
            res=res+right[j:]
        else:
            res=res+left[i:]
        return res
    def quicksort(self,arr):
        if len(arr)==0 or len(arr)==1:
            return arr
        elif len(arr)==2:
            if arr[0]>arr[1]:
                arr[0],arr[1]=arr[1],arr[0]
            return arr
        else:
            mid=len(arr)//2
            left=self.quicksort(arr[:mid])
            right=self.quicksort(arr[mid:])
            arr=self.merge(left,right)
            return arr
    
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if len(arr)==0 or k==0:
            return []
        elif len(arr)==1 and k==1:
            return arr
        else:
            arr=self.quicksort(arr)
            return arr[:k]
    