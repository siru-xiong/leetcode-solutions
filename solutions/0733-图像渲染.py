# Problem Id:  733
# Problem Name:  Flood Fill, 图像渲染
# Problem Url:  https://leetcode-cn.com/problems/flood-fill/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        xmax = len(image) - 1
        ymax = len(image[0]) - 1
        record = []
        def rec(x,y):
            if [x,y] in record:
                pass
            else:
                record.append([x,y])
                if x+1 <= xmax and image[x+1][y] == image[x][y]:
                    rec(x+1,y)
                if x-1 >= 0 and image[x-1][y] == image[x][y]:
                    rec(x-1,y)                
                if y+1 <= ymax and image[x][y+1] == image[x][y]:
                    rec(x,y+1)                
                if y-1 >= 0 and image[x][y-1] == image[x][y]:
                    rec(x,y-1)
        rec(sr,sc)
        for i in range(len(record)):
            image[record[i][0]][record[i][1]] = newColor
        return image

            

