################ DFS ###########################
class Solution {
public:
    void dfs (vector<vector<int>>& rooms, vector<bool> &visited, int source){
        visited[source] = true;
        
        for(int &nodes: rooms[source]){
            if(!visited[nodes]){
                dfs(rooms, visited, nodes);
            }
        }
    }
    
    
    
    
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        vector<bool> visited(n, false);
        
        
        dfs(rooms, visited, 0);
        
        for(bool x:visited){
            if(x==false){
                return false;
        }}
        
        return true;
        
        
        
    }
};


########################### BFS ##########################

class Solution {
public:
   bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        vector<bool> visited(n, false);
        queue<int> q;
        q.push(0);
        visited[0] = true;
       
       while(!q.empty()){
           int node = q.front();
           q.pop();
           for(auto it: rooms[node]){
               if(!visited[it]){
                   q.push(it);
                   visited[it]=true;
               }
           }
           
       }
       
       
       
        
       
        
        for(bool x:visited){
            if(x==false){
                return false;
        }}
        
        return true;
        
        
        
    }
};