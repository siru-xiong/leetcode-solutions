# Problem Id:  1640
# Problem Name:  Check Array Formation Through Concatenation, 能否连接形成数组
# Problem Url:  https://leetcode-cn.com/problems/check-array-formation-through-concatenation/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        while True:
            i = 1
            k = len(arr)
            while True:
                if arr[:i] in pieces:
                    for j in range(len(pieces)):
                        if pieces[j] == arr[:i]:
                            del pieces[j]
                            break
                    arr = arr[i:]        
                    break
                else:
                    i = i + 1
                if i == len(arr)+1:
                    break
            if arr == [] or len(arr) == k:
                break
        return arr == [] and len(pieces) == 0