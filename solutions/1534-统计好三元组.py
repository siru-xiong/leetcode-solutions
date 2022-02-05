# Problem Id:  1534
# Problem Name:  Count Good Triplets, 统计好三元组
# Problem Url:  https://leetcode-cn.com/problems/count-good-triplets/
# Problem Level:  Easy
 
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0
        for i in range(len(arr)-2):
            for j in range(i+1,len(arr)-1):
                if abs(arr[j] - arr[i]) <= a:
                    for k in range(j+1,len(arr)):
                        if abs(arr[k] - arr[j]) <= b and abs(arr[k] - arr[i]) <= c:
                            res += 1
        return res
