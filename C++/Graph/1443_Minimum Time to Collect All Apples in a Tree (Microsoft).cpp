class Solution {
public:
    
    int dfs(unordered_map<int, vector<int>> &adj, vector<bool>& hasApple, int node, int parent){
        int totaltime = 0; int childtime = 0;
        
        
        for(auto child:adj[node]){
            if(child==parent)
                continue;
            childtime = dfs(adj, hasApple, child, node);
            if(childtime > 0 || hasApple[child])
                totaltime += childtime + 2;  
            
            
        }
        
        
        
        return totaltime;
        
    }
    
    
    
    
    int minTime(int n, vector<vector<int>>& edges, vector<bool>& hasApple) {
        unordered_map<int, vector<int>> adj;
        for(auto vec:edges){
            adj[vec[0]].push_back(vec[1]);
            adj[vec[1]].push_back(vec[0]);            
        }
        
        return dfs(adj, hasApple,0,-1);
    }
    
    
    
    
};