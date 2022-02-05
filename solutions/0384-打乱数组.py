# Problem Id:  384
# Problem Name:  Shuffle an Array, 打乱数组
# Problem Url:  https://leetcode-cn.com/problems/shuffle-an-array/
# Problem Level:  Medium
 
class Solution:

    def __init__(self, nums: List[int]):
        self.origin = nums
        self.new = [i for i in nums]


    def reset(self) -> List[int]:
        self.new = [i for i in self.origin]
        return self.new


    def shuffle(self) -> List[int]:
        for i in range(len(self.new)):
            t = random.randint(i,len(self.new)-1)
            self.new[i],self.new[t] = self.new[t],self.new[i]
        return self.new




# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()