# Problem Id:  599
# Problem Name:  Minimum Index Sum of Two Lists, 两个列表的最小索引总和
# Problem Url:  https://leetcode-cn.com/problems/minimum-index-sum-of-two-lists/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        l1 = {}
        result = []
        vmin = float('inf')
        for i in range(len(list1)):
            l1[list1[i]] = i
        for i in range(len(list2)):
            if list2[i] in l1:
                l1[list2[i]] = l1[list2[i]] + i
                if l1[list2[i]] < vmin:
                    result = []
                    result.append(list2[i])
                    vmin = l1[list2[i]]
                elif l1[list2[i]] == vmin:
                    result.append(list2[i])
        return result