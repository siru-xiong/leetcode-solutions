// Problem Id:  剑指 Offer 65
// Problem Name:  不用加减乘除做加法 LCOF, 不用加减乘除做加法
// Problem Url:  https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/
// Problem Level:  Easy
// Language:  Java
 
class Solution {
    public int add(int a, int b) {
        while(b != 0) { // 当进位为 0 时跳出
            int c = (a & b) << 1;  // c = 进位
            a ^= b; // a = 非进位和
            b = c; // b = 进位
        }
        return a;
    }
}