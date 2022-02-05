# Problem Id:  1299
# Problem Name:  Replace Elements with Greatest Element on Right Side, 将每个元素替换为右侧最大元素
# Problem Url:  https://leetcode-cn.com/problems/replace-elements-with-greatest-element-on-right-side/
# Problem Level:  Easy
 
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        start = -1
        for i in range(len(arr)-1,-1,-1):
            temp = arr[i]
            arr[i] = start
            if temp > start:
                start = temp
        return arr