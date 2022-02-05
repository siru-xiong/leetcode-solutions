# Problem Id:  239
# Problem Name:  Sliding Window Maximum, 滑动窗口最大值
# Problem Url:  https://leetcode-cn.com/problems/sliding-window-maximum/
# Problem Level:  Hard
 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        q = []
        res = []
        for i in range(len(nums)):
            if i > 0:
                while len(q) > 0 and q[-1] < nums[i]:
                    q = q[:(-1)]
            q.append(nums[i])
            if i >= k and nums[i-k] == q[0]:
                q = q[1:]
            if i >= k-1:
                res.append(q[0])
        return res        
