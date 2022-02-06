// Problem Id:  1093
// Problem Name:  Statistics from a Large Sample, 大样本统计
// Problem Url:  https://leetcode-cn.com/problems/statistics-from-a-large-sample/
// Problem Level:  Medium
// Language:  C++
 
class Solution {
public:
    vector<double> sampleStats(vector<int>& count) {
        double mini = -1;
        double maxi;
        double mean;
        double median;
        double mode;
        int mc = -1;
        double sum = 0;
        int c = 0;
        for (int i=0;i<count.size();i++) {
            if (count[i] > 0) {
                if (mini == -1) {
                    mini = i;
                }
                maxi = i;
                c += count[i];
                sum += (double)count[i]*i;
                if (count[i] > mc) {
                    mode = i;
                    mc = count[i];
                }
            }
        }
        mean = sum / c;
        if (c % 2 == 0) {
            int midCnt = c >> 1;
            int left = 0;
            int right = 0;
            int cnt = 0;
            int index = 0;
            for (int j=0;j<count.size();j++) {
                if (count[j] > 0) {
                    if (index == 1) {
                        right = j;
                        break;
                    }
                    cnt += count[j];
                    if (cnt > midCnt) {
                        left = j;
                        right = j;
                        break;
                    }
                    if (cnt == midCnt) {
                        left = j;
                        index = 1;
                    } 
                }
            }
            median = (left+right) / 2.0;
        } else {
            int midCnt = (c >> 1) + 1;
            int left = 0;
            int cnt = 0;
            for (int j=0;j<count.size();j++) {
                cnt += count[j];
                if (cnt >= midCnt) {
                    left = j;
                    break;
                }
            }
            median = left;
        }
        return {(double)mini, maxi, mean, median, mode};
    }
};