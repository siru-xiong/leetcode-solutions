# Problem Id:  1603
# Problem Name:  Design Parking System, 设计停车系统
# Problem Url:  https://leetcode-cn.com/problems/design-parking-system/
# Problem Level:  Easy
# Language:  Python3
 
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.record = [big,medium,small]


    def addCar(self, carType: int) -> bool:
        if self.record[carType-1] > 0:
            self.record[carType-1] -= 1
            return True
        else:
            return False




# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)