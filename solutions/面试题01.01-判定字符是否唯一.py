# Problem Id:  面试题 01.01
# Problem Name:  Is Unique LCCI, 判定字符是否唯一
# Problem Url:  https://leetcode-cn.com/problems/is-unique-lcci/
# Problem Level:  Easy
 
class Solution:
    def isUnique(self, astr: str) -> bool:
        return len(set(astr)) == len(astr)