# Problem Id:  剑指 Offer II 059
# Problem Name:  数据流的第 K 大数值, 数据流的第 K 大数值
# Problem Url:  https://leetcode-cn.com/problems/jBjn9C/
# Problem Level:  Easy
 
class KthLargest {
public:
    priority_queue<int, vector<int>, greater<int>> q;
    int k;
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for (auto& x: nums) {
            add(x);
        }
    }
    
    int add(int val) {
        q.push(val);
        if (q.size() > k) {
            q.pop();
        }
        return q.top();
    }
};