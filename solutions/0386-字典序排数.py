# Problem Id:  386
# Problem Name:  Lexicographical Numbers, 字典序排数
# Problem Url:  https://leetcode-cn.com/problems/lexicographical-numbers/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(list(range(1,n+1)),key=str)