#################### DFS #############################
class Solution {
public:
    void dfs(vector<vector<int>>& graph, int u, int t, vector<vector<int>>& result,vector<int>& temp){
        temp.push_back(u);
        if(u==t){
            result.push_back(temp);
        }
        else{
            for(int &v:graph[u]){
                dfs(graph, v, t, result, temp);        
            }
        }
        
        temp.pop_back();
        
    }
    
    
    
    
    
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        int n = graph.size();
        
        int source = 0;
        int target = n-1;
        vector<vector<int>> result;
        vector<int> temp;
        
        
        dfs(graph, source, target, result, temp);
        
        return result;
    }
};

################################## BFS #######################################
class Solution {
public:
vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        int n = graph.size();
        queue<vector<int>> q;
        vector<vector<int>> ans;
    
        q.push({0});
    
    while(!q.empty()){
        vector<int> path = q.front();
        
        q.pop();
        
        if(path.back()== n-1){
            ans.push_back(path);
        }
        else
        for (auto child:graph[path.back()]){
            path.push_back(child);
            q.push(path);
            path.pop_back();
        }
    }
    return ans;        
    
    }
};