# Problem Id:  500
# Problem Name:  Keyboard Row, 键盘行
# Problem Url:  https://leetcode-cn.com/problems/keyboard-row/
# Problem Level:  Easy
 
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set(list("qwertyuiop"))
        row2 = set(list("asdfghjkl"))
        row3 = set(list("zxcvbnm"))
        result = []
        for i in range(len(words)):
            l = words[i].lower()
            if (set(list(l)) & row1 == set(list(l))) or (set(list(l)) & row2 == set(list(l))) or (set(list(l)) & row3 == set(list(l))):
                result.append(words[i])
        return result