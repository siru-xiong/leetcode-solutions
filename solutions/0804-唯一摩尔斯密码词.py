# Problem Id:  804
# Problem Name:  Unique Morse Code Words, 唯一摩尔斯密码词
# Problem Url:  https://leetcode-cn.com/problems/unique-morse-code-words/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        m = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = []
        for i in words:
            t = ''
            for j in i:
                t = t + m[ord(j)-ord('a')]
            res.append(t)
        return len(set(res))
