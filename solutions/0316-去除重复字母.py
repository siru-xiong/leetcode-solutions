# Problem Id:  316
# Problem Name:  Remove Duplicate Letters, 去除重复字母
# Problem Url:  https://leetcode-cn.com/problems/remove-duplicate-letters/
# Problem Level:  Medium
 
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic = {}
        for i in s:
            dic[i] = dic.get(i,0) + 1
        st = []
        sd = {}
        for i in s:
            if sd.get(i,0) == 0:
                if len(st) == 0:
                    st.append(i)
                    sd[i] = sd.get(i,0)+1
                    dic[i] -= 1
                else:
                    while len(st) > 0 and st[-1] > i and dic.get(st[-1],0) > 0:
                        sd[st[-1]] = sd.get(st[-1],0)-1
                        del st[-1]
                    st.append(i)
                    sd[i] = sd.get(i,0)+1
                    dic[i] -= 1
            else:
                dic[i] -= 1
        return ''.join(st)