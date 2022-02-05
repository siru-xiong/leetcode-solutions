# Problem Id:  710
# Problem Name:  Random Pick with Blacklist, 黑名单中的随机数
# Problem Url:  https://leetcode-cn.com/problems/random-pick-with-blacklist/
# Problem Level:  Hard
 
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.map = dict()
        self.size = n - len(blacklist)
        white_set = set(range(n - len(blacklist),n))
        for i in blacklist:
            if i in white_set:
                white_set.remove(i)
        white_set = list(white_set)
        j = 0
        for i in blacklist:
            if i < n - len(blacklist):
                self.map[i] = white_set[j]
                j += 1 

    def pick(self) -> int:
        res = random.randint(0,self.size-1)
        return self.map.get(res,res)



# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()