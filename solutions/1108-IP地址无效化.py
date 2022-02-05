# Problem Id:  1108
# Problem Name:  Defanging an IP Address, IP 地址无效化
# Problem Url:  https://leetcode-cn.com/problems/defanging-an-ip-address/
# Problem Level:  Easy
 
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return '[.]'.join(address.split('.'))