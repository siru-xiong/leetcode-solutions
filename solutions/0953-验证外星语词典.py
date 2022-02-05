# Problem Id:  953
# Problem Name:  Verifying an Alien Dictionary, 验证外星语词典
# Problem Url:  https://leetcode-cn.com/problems/verifying-an-alien-dictionary/
# Problem Level:  Easy
 
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        normal = 'abcdefghijklmnopqrstuvwxyz'
        func = {}
        for i in range(26):
            func[order[i]] = normal[i]
        for i in range(len(words)):
            temp = list(words[i])
            for j in range(len(temp)):
                temp[j] = func[temp[j]]
            words[i]=''.join(temp)
        return sorted(words) == words