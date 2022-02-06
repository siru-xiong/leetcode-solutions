# Problem Id:  744
# Problem Name:  Find Smallest Letter Greater Than Target, 寻找比目标字母大的最小字母
# Problem Url:  https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target < letters[0] or target >= letters[-1]:
            return letters[0]
        else:
            left = 0
            right = len(letters)-1
            while right-left>=2:
                med = int((left+right)/2)
                if letters[med] > target:
                    right = med
                elif letters[med] <= target:
                    left = med
            if letters[left] > target:
                return letters[left]
            else:
                return letters[right]
