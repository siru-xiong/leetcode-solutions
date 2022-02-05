# Problem Id:  703
# Problem Name:  Kth Largest Element in a Stream, 数据流中的第 K 大元素
# Problem Url:  https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/
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
