# Problem Id:  1710
# Problem Name:  Maximum Units on a Truck, 卡车上的最大单元数
# Problem Url:  https://leetcode-cn.com/problems/maximum-units-on-a-truck/
# Problem Level:  Easy
 
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        result = 0
        num = 0
        i = 0
        while num<truckSize and i < len(boxTypes):
            nnum = min(truckSize-num,boxTypes[i][0])
            num = num + nnum
            result = result + nnum*boxTypes[i][1]
            i = i + 1
        return result

