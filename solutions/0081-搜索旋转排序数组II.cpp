# Problem Id:  81
# Problem Name:  Search in Rotated Sorted Array II, 搜索旋转排序数组 II
# Problem Url:  https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/
# Problem Level:  Medium
 
class Solution {
public:
    bool search(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++) 
            if (nums[i] == target)
                return true;
        return false;
    }
};