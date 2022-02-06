// Problem Id:  684
// Problem Name:  Redundant Connection, 冗余连接
// Problem Url:  https://leetcode-cn.com/problems/redundant-connection/
// Problem Level:  Medium
// Language:  C++
 
class UnionFind{
public:
    int find(int x){
        int root = x;
        while(father[root] != -1){
            root = father[root];
        }
        
        while(x != root){
            int original_father = father[x];
            father[x] = root;
            x = original_father;
        } 
        return root;
    }
    
    bool is_connected(int x,int y){
        return find(x) == find(y);
    }
    
    void merge(int x,int y){
        int root_x = find(x);
        int root_y = find(y);
        if(root_x != root_y){
            father[root_x] = root_y;
        }
    }
    
    void add(int x){
        if(!father.count(x)){
            father[x] = -1;
        }
    }
    
private:
    unordered_map<int,int> father;
};

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        UnionFind uf;
        for (int i = 0;i < edges.size();i++) {
            uf.add(edges[i][0]);
            uf.add(edges[i][1]);
            if (uf.is_connected(edges[i][0],edges[i][1])) {
                return edges[i];
            } else {
                uf.merge(edges[i][0],edges[i][1]);
            }
        }
        return {};
    }
};