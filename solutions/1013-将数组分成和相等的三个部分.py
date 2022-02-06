# Problem Id:  1013
# Problem Name:  Partition Array Into Three Parts With Equal Sum, 将数组分成和相等的三个部分
# Problem Url:  https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        t = sum(arr)
        if t % 3 != 0:
            return False
        t = t // 3
        s = 0
        i1 = -1
        for i in range(len(arr)):
            s = s + arr[i]
            if s == t:
                i1 = i
                break
        if i1 == -1:
            return False
        s = 0
        i2 = -1
        for j in range(i1+1,len(arr)):
            s = s + arr[j]
            if s == t:
                i2 = j
                break
        if i2 == -1:
            return False
        return sum(arr[(i2+1):]) == t and i2 != len(arr)-1