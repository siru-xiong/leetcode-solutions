// Problem Id:  剑指 Offer II 072
// Problem Name:  求平方根, 求平方根
// Problem Url:  https://leetcode-cn.com/problems/jJ0w9p/
// Problem Level:  Easy
// Language:  C++
 
class Solution {
public:
    int mySqrt(int x) {
        if (x == 0) {
            return 0;
        } else if (x<=3) {
            return 1;
        } else {
            int left = 1;
            int right = x >> 1;
            while (left <= right) {
                int mid = left + ((right - left) >> 1);
                if (mid <= x / mid) {
                   if (mid + 1 > x / (mid + 1)) {
                     return mid;
                    }
                    left = mid + 1;
                } else {
                    right = mid - 1;
               }
            }
        }
        return 0;
    }
};