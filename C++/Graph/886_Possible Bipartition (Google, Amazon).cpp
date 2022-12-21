###################################### DFS ##################################

class Solution {
public:
    bool dfs(unordered_map <int, vector<int>> &adj, vector<int> &color, int node, int nodecolor){
        color[node] = nodecolor;
        
        for(auto& nei: adj[node]){
            if (color[nei] == color[node]) return false;
            if(color[nei]==-1){
                if(!dfs(adj, color, nei,  1-color[node])) return false;
            }
        }
        
        return true;
        
    }
    
    
    
    
    bool possibleBipartition(int n, vector<vector<int>>& dislikes) {
        vector<int> color(n+1, -1);
        unordered_map <int, vector<int>> adj;
        
        for(vector<int> &it: dislikes){
            int u = it[0];
            int v = it[1];
            
            adj[u].push_back(v);
            adj[v].push_back(u);
            }
        
        for(int i = 1 ; i <= n;i++ ){
            if(color[i]==- 1){
                if(!dfs(adj, color, i,0))
                    return false;
            }
        }
        return true;
    }
};


###################################### BFS ##################################

class Solution {
public:
    bool bfs(unordered_map <int, vector<int>> &adj, vector<int> &color, int source){
        queue<int> q;
        
        q.push(source);
        color[source] = 0;
        
        while(!q.empty()){
            int node = q.front();
            q.pop();
                
            for(auto &nei: adj[node]){
                if(color[nei]==color[node]) return false;
                if(color[nei]==-1){
                    color[nei] = 1 - color[node];
                    q.push(nei);
                }
            }
        }
        
        return true;
        
    }
    
    
    
    
    bool possibleBipartition(int n, vector<vector<int>>& dislikes) {
        vector<int> color(n+1, -1);
        unordered_map <int, vector<int>> adj;
        
        for(vector<int> &it: dislikes){
            int u = it[0];
            int v = it[1];
            
            adj[u].push_back(v);
            adj[v].push_back(u);
            }
        
        for(int i = 1 ; i <= n;i++ ){
            if(color[i]==- 1){
                if(!bfs(adj, color, i))
                    return false;
            }
        }
        return true;
    }
};