// Problem Id:  275
// Problem Name:  H-Index II, H 指数 II
// Problem Url:  https://leetcode-cn.com/problems/h-index-ii/
// Problem Level:  Medium
// Language:  C++
 
class Solution {
public:
    int hIndex(vector<int>& citations) {
        int l = 0;
        int length = citations.size();
        int r = length-1;
        int mid = l;
        while (r > l+1) {
            mid = (l+r) / 2;
            if (citations[mid] <= length-mid) {
                l = mid;
            } else {
                r = mid;
            }
        }
        if (citations[r] <= length-r) {
            return citations[r];
        } else if (citations[l] <= length-l) {
            return max(citations[l],length-r);
        } else {
            return length;
        }
        return 0;
    }
};