# Problem Id:  93
# Problem Name:  Restore IP Addresses, 复原 IP 地址
# Problem Url:  https://leetcode-cn.com/problems/restore-ip-addresses/
# Problem Level:  Medium
 
class Solution:
    def restoreIpAddresses(self, s: str, k=4) -> List[str]:
        if k == 1:
            if len(s) == 0:
                return []
            elif (int(s) >= 0 and int(s) <= 255 and s[0]!='0') or s == '0':
                    return [s]
            else:
                return []
        else:
            res = []
            for i in range(1,len(s)+1):
                if (int(s[:i]) >= 0 and int(s[:i]) <= 255 and s[0]!='0') or (s[0] == '0' and i == 1):
                    r = self.restoreIpAddresses(s[i:],k-1)
                    if len(r) != 0:
                        for j in r:
                            res.append(s[:i]+'.'+j)
            return res
        
        