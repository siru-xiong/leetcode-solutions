# Problem Id:  面试题 03.06
# Problem Name:  Animal Shelter LCCI, 动物收容所
# Problem Url:  https://leetcode-cn.com/problems/animal-shelter-lcci/
# Problem Level:  Easy
# Language:  Python3
 
class AnimalShelf:

    def __init__(self):
        self.cat = []
        self.dog = []
        self.num = []

    def enqueue(self, animal: List[int]) -> None:
        if animal[1] == 0:
            self.cat.append(animal[0])
        if animal[1] == 1:
            self.dog.append(animal[0])


    def dequeueAny(self) -> List[int]:
        if len(self.cat) == 0:
            return self.dequeueDog()
        elif len(self.dog) == 0:
            return self.dequeueCat()
        else:
            if self.cat[0] < self.dog[0]:
                return self.dequeueCat()
            else:
                return self.dequeueDog()


    def dequeueDog(self) -> List[int]:
        if len(self.dog) == 0:
            return [-1,-1]
        else:
            t = self.dog[0]
            del self.dog[0]
            return [t,1]

    def dequeueCat(self) -> List[int]:
        if len(self.cat) == 0:
            return [-1,-1]
        else:
            t = self.cat[0]
            del self.cat[0]
            return [t,0]



# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()