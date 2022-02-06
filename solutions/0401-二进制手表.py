# Problem Id:  401
# Problem Name:  Binary Watch, 二进制手表
# Problem Url:  https://leetcode-cn.com/problems/binary-watch/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def light(self,num,vlist):
        if num == 0:
            return [0]
        elif len(vlist) == 1 and num == 1:
            return [vlist[0]]
        elif num > len(vlist):
            return []
        else:
            return [i+vlist[0] for i in self.light(num-1,vlist[1:])] + self.light(num,vlist[1:])

    def readBinaryWatch(self, num: int) -> List[str]:
        result = []
        for i in range(num+1):
            #up i
            #down num-i
            up = [str(i) for i in self.light(i,[8,4,2,1]) if i <= 11 and i >= 0]
            down = [i for i in self.light(num-i,[32,16,8,4,2,1]) if i<=59 and i>=0]
            for j in range(len(down)):
                if down[j] == 0:
                    down[j] = '00'
                elif down[j] <= 9:
                    down[j] = '0'+str(down[j])
                else:
                    down[j] = str(down[j])
            result = result + [x+":"+y for x in up for y in down]
        return result


