# Problem Id:  661
# Problem Name:  Image Smoother, 图片平滑器
# Problem Url:  https://leetcode-cn.com/problems/image-smoother/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        x = len(M)
        y = len(M[0])
        result = [[0]*(y) for _ in range(x)]
        for i in range(x):
            for j in range(y):
                count = 0
                v = 0
                for m in (i-1,i,i+1):
                    for n in (j-1,j,j+1):
                        if 0 <= m and m <= x-1 and 0 <= n and n <= y-1:
                            count = count + 1
                            v = v + M[m][n]
                result[i][j] = int(v / count)
                
        return result