# Problem Id:  1720
# Problem Name:  Decode XORed Array, 解码异或后的数组
# Problem Url:  https://leetcode-cn.com/problems/decode-xored-array/
# Problem Level:  Easy
 
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for i in encoded:
            res.append(res[-1]^i)
        return res