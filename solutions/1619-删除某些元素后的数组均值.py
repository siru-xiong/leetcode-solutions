# Problem Id:  1619
# Problem Name:  Mean of Array After Removing Some Elements, 删除某些元素后的数组均值
# Problem Url:  https://leetcode-cn.com/problems/mean-of-array-after-removing-some-elements/
# Problem Level:  Easy
 
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        t = len(arr) // 20
        return sum(arr[t:(len(arr)-t)]) / (len(arr)-2*t)