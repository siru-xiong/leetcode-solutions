# Problem Id:  547
# Problem Name:  Number of Provinces, 省份数量
# Problem Url:  https://leetcode-cn.com/problems/number-of-provinces/
# Problem Level:  Medium
 
class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int provinces = isConnected.size();
        vector<int> visited(provinces);
        int circles = 0;
        queue<int> Q;
        for (int i = 0; i < provinces; i++) {
            if (visited[i]==0) {
                Q.push(i);
                while (!Q.empty()) {
                    int j = Q.front();
                    visited[j] = 1;
                    Q.pop();
                    for (int k = 0;k < provinces;k++) {
                        if (visited[k]==0 and isConnected[j][k]==1) {
                            Q.push(k);
                        }
                    }
                }
                circles++;
            }
        }
        return circles;
    }
};