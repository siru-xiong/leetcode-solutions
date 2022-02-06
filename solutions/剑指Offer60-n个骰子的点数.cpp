// Problem Id:  剑指 Offer 60
// Problem Name:  n个骰子的点数  LCOF, n个骰子的点数
// Problem Url:  https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/
// Problem Level:  Medium
// Language:  C++
 
class Solution {
public:
    vector<double> dicesProbability(int n) {
        double x = 1.0/6;
        vector<double> base(6,x);
        vector<double> res(6,x);
        for (int i =0;i < n-1;i++) {
            res = comp(res,base);
        }
        return res;
    }
    vector<double> comp(vector<double> a,vector<double> b) {
        int m = a.size();
        int n = b.size();
        vector<double> res(m+n-1,0);
        for (int i = 0;i < m+n;i++) {
            for (int j =0;j < i+1;j++) {
                if (j < m && i-j < n) {
                    res[i] += a[j]*b[i-j];
                }
            }
        }
        return res;
    }
};