# Problem Id:  剑指 Offer II 030
# Problem Name:  插入、删除和随机访问都是 O(1) 的容器, 插入、删除和随机访问都是 O(1) 的容器
# Problem Url:  https://leetcode-cn.com/problems/FortPu/
# Problem Level:  Medium
# Language:  Python3
 
class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.rec = []


    def insert(self, val: int) -> bool:
        if val not in self.dic:
            self.rec.append(val)
            self.dic[val]=len(self.rec)-1
            return True
        else:
            return False



    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        else:
            if len(self.rec) == 1:
                self.rec = []
                self.dic = {}
                return True
            else:
                t = self.dic[val]
                self.rec[t] = self.rec[-1]
                self.dic[self.rec[-1]] = t
                del self.rec[-1]
                del self.dic[val]
                return True

    def getRandom(self) -> int:
        return choice(self.rec)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()