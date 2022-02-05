# Problem Id:  剑指 Offer 56 - II
# Problem Name:  数组中数字出现的次数 II LCOF, 数组中数字出现的次数 II
# Problem Url:  https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/
# Problem Level:  Medium
 
class Solution:
    def bina(self,number):
        i = 0
        r = 1
        while r*2 <= number:
            r = r*2
            i = i + 1
        res = []
        while i >= 0:
            if number >= r:
                res = res + [1]
                number = number - r
                r = r // 2
                i = i - 1
            else:
                res = res + [0]
                r = r // 2
                i = i - 1
        return res
            
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            r = self.bina(i)
            for i in range(1,len(r)+1):
                dic[i-1] = dic.get(i-1,0) + r[-i]
        res = 0
        print(dic)
        for i in dic:
            if dic[i] % 3 != 0:
                res = res + 2**i
        return res
                