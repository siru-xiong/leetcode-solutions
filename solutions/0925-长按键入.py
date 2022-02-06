# Problem Id:  925
# Problem Name:  Long Pressed Name, 长按键入
# Problem Url:  https://leetcode-cn.com/problems/long-pressed-name/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        result = True
        while i < len(name) and j < len(typed) :
            if name[i] != typed[j]:
                result = False
                break
            else:
                x = 0
                while i + 1 + x < len(name) and name[i+1+x] == name[i]:
                    x = x + 1
                i = i + x + 1
                y = 0
                while j + 1 + y < len(typed) and typed[j+1+y] == typed[j]:
                    y = y + 1
                j = j + y + 1
                if y < x:
                    result = False
                    break
        return result and i >= len(name) and j >= len(typed)
