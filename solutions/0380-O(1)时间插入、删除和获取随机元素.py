# Problem Id:  380
# Problem Name:  Insert Delete GetRandom O(1), O(1) 时间插入、删除和获取随机元素
# Problem Url:  https://leetcode-cn.com/problems/insert-delete-getrandom-o1/
# Problem Level:  Medium
 
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
