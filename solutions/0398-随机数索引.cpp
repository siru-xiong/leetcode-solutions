# Problem Id:  398
# Problem Name:  Random Pick Index, 随机数索引
# Problem Url:  https://leetcode-cn.com/problems/random-pick-index/
# Problem Level:  Medium
 
class Solution {
public:
    vector<int> rec;
    Solution(vector<int>& nums) {
        rec = nums;
    }
    
    int pick(int target) {
        int res = 0;
        int c = 0;
        for (int i = 0;i < rec.size();i++) {
            if (rec[i]== target) {
                c ++;
                if (rand() % c == 0) {
                    res = i;
                }
            }
        }
        return res;

    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * int param_1 = obj->pick(target);
 */